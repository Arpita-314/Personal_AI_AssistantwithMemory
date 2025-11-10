import React, { useState, useEffect, useRef } from 'react';
import { Brain, Lock, Send, Trophy, Zap, Sword, Heart, Star, Sparkles, Key, Volume2 } from 'lucide-react';
import * as d3 from 'd3';

const MemoryGardenRPG = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [encryptionKey, setEncryptionKey] = useState(null);
  const [showSetup, setShowSetup] = useState(true);
  const [password, setPassword] = useState('');
  const [nodes, setNodes] = useState([]);
  const [links, setLinks] = useState([]);
  const [selectedNode, setSelectedNode] = useState(null);
  const [playerStats, setPlayerStats] = useState({
    level: 1,
    xp: 0,
    thoughtsSaved: 0,
    bossesDefeated: 0,
    connectionsCreated: 0,
    streak: 0
  });
  const [achievements, setAchievements] = useState([]);
  const [showAchievement, setShowAchievement] = useState(null);
  const [aiMood, setAiMood] = useState('curious');
  const [currentBattle, setCurrentBattle] = useState(null);
  const svgRef = useRef(null);
  const simulationRef = useRef(null);

  const ACHIEVEMENTS = [
    { id: 'first_thought', name: 'First Seed', desc: 'Plant your first thought', icon: '🌱', threshold: 1, stat: 'thoughtsSaved' },
    { id: 'gardener', name: 'Thought Gardener', desc: 'Save 10 thoughts', icon: '🌿', threshold: 10, stat: 'thoughtsSaved' },
    { id: 'connector', name: 'Synapse Builder', desc: 'Create 5 connections', icon: '🧠', threshold: 5, stat: 'connectionsCreated' },
    { id: 'warrior', name: 'Overthinking Slayer', desc: 'Defeat your first boss', icon: '⚔️', threshold: 1, stat: 'bossesDefeated' },
    { id: 'streak', name: 'Consistent Thinker', desc: 'Use 3 days in a row', icon: '🔥', threshold: 3, stat: 'streak' },
    { id: 'master', name: 'Memory Master', desc: 'Reach level 5', icon: '👑', threshold: 5, stat: 'level' }
  ];

  useEffect(() => {
    checkExistingData();
    checkStreak();
  }, []);

  const checkStreak = async () => {
    try {
      const lastVisit = await window.storage.get('last-visit');
      const today = new Date().toDateString();
      
      if (lastVisit) {
        const lastDate = new Date(lastVisit.value);
        const yesterday = new Date();
        yesterday.setDate(yesterday.getDate() - 1);
        
        if (lastDate.toDateString() === yesterday.toDateString()) {
          setPlayerStats(prev => ({ ...prev, streak: prev.streak + 1 }));
        } else if (lastDate.toDateString() !== today) {
          setPlayerStats(prev => ({ ...prev, streak: 1 }));
        }
      }
      
      await window.storage.set('last-visit', today);
    } catch (err) {
      console.log('Streak check error:', err);
    }
  };

  const checkExistingData = async () => {
    try {
      const stored = await window.storage.get('encrypted-chats');
      if (stored) {
        setShowSetup(true);
      }
    } catch (err) {
      console.log('No existing data');
    }
  };

  const deriveKey = async (pwd) => {
    const encoder = new TextEncoder();
    const data = encoder.encode(pwd);
    const hash = await crypto.subtle.digest('SHA-256', data);
    return await crypto.subtle.importKey('raw', hash, { name: 'AES-GCM' }, false, ['encrypt', 'decrypt']);
  };

  const encryptData = async (data, key) => {
    const encoder = new TextEncoder();
    const iv = crypto.getRandomValues(new Uint8Array(12));
    const encrypted = await crypto.subtle.encrypt(
      { name: 'AES-GCM', iv },
      key,
      encoder.encode(JSON.stringify(data))
    );
    return { iv: Array.from(iv), data: Array.from(new Uint8Array(encrypted)) };
  };

  const decryptData = async (encrypted, key) => {
    try {
      const decrypted = await crypto.subtle.decrypt(
        { name: 'AES-GCM', iv: new Uint8Array(encrypted.iv) },
        key,
        new Uint8Array(encrypted.data)
      );
      const decoder = new TextDecoder();
      return JSON.parse(decoder.decode(decrypted));
    } catch (err) {
      throw new Error('Decryption failed');
    }
  };

  const handleSetup = async () => {
    if (password.length < 6) {
      alert('Password must be at least 6 characters');
      return;
    }
    
    const key = await deriveKey(password);
    setEncryptionKey(key);
    
    try {
      const stored = await window.storage.get('encrypted-chats');
      if (stored) {
        const decrypted = await decryptData(JSON.parse(stored.value), key);
        setMessages(decrypted.messages || []);
        setNodes(decrypted.nodes || []);
        setLinks(decrypted.links || []);
        setPlayerStats(decrypted.playerStats || playerStats);
        setAchievements(decrypted.achievements || []);
      }
    } catch (err) {
      alert('Wrong password');
      return;
    }
    
    setShowSetup(false);
    setPassword('');
  };

  const saveData = async (msgs, nds, lnks, stats, achs) => {
    if (!encryptionKey) return;
    
    const data = { messages: msgs, nodes: nds, links: lnks, playerStats: stats, achievements: achs };
    const encrypted = await encryptData(data, encryptionKey);
    await window.storage.set('encrypted-chats', JSON.stringify(encrypted));
  };

  const unlockAchievement = (achievement) => {
    if (!achievements.includes(achievement.id)) {
      const newAchievements = [...achievements, achievement.id];
      setAchievements(newAchievements);
      setShowAchievement(achievement);
      playSound('achievement');
      setTimeout(() => setShowAchievement(null), 3000);
      return newAchievements;
    }
    return achievements;
  };

  const checkAchievements = (stats, achs) => {
    let updatedAchs = achs;
    ACHIEVEMENTS.forEach(achievement => {
      if (stats[achievement.stat] >= achievement.threshold) {
        updatedAchs = unlockAchievement(achievement) || updatedAchs;
      }
    });
    return updatedAchs;
  };

  const addXP = (amount, stats) => {
    const newXP = stats.xp + amount;
    const newLevel = Math.floor(newXP / 100) + 1;
    const leveledUp = newLevel > stats.level;
    
    if (leveledUp) {
      playSound('levelup');
      updateAiMood('excited');
    }
    
    return { ...stats, xp: newXP, level: newLevel };
  };

  const playSound = (type) => {
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    if (type === 'achievement') {
      oscillator.frequency.value = 800;
      gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
      gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.5);
      oscillator.start(audioContext.currentTime);
      oscillator.stop(audioContext.currentTime + 0.5);
    } else if (type === 'levelup') {
      [523, 659, 784].forEach((freq, i) => {
        const osc = audioContext.createOscillator();
        const gain = audioContext.createGain();
        osc.connect(gain);
        gain.connect(audioContext.destination);
        osc.frequency.value = freq;
        gain.gain.setValueAtTime(0.2, audioContext.currentTime + i * 0.1);
        gain.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + i * 0.1 + 0.3);
        osc.start(audioContext.currentTime + i * 0.1);
        osc.stop(audioContext.currentTime + i * 0.1 + 0.3);
      });
    }
  };

  const updateAiMood = (mood) => {
    setAiMood(mood);
    setTimeout(() => setAiMood('curious'), 3000);
  };

  const getMoodEmoji = () => {
    const moods = {
      curious: '🤔',
      excited: '🎉',
      supportive: '💪',
      thoughtful: '💭',
      celebrating: '🌟'
    };
    return moods[aiMood] || '🤖';
  };

  const extractConcepts = (text) => {
    const words = text.toLowerCase().split(/\W+/).filter(w => w.length > 4);
    return [...new Set(words)].slice(0, 3);
  };

  const detectOverthinking = (text) => {
    const overthinkingWords = ['worry', 'anxious', 'stress', 'overthink', 'cant stop', 'stuck', 'confused', 'overwhelmed'];
    return overthinkingWords.some(word => text.toLowerCase().includes(word));
  };

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const isOverthinking = detectOverthinking(input);
    
    if (isOverthinking && !currentBattle) {
      setCurrentBattle({
        thought: input,
        hp: 100,
        playerHp: 100
      });
      return;
    }

    const userMsg = { role: 'user', content: input, timestamp: Date.now() };
    const newMessages = [...messages, userMsg];
    setMessages(newMessages);
    setLoading(true);
    setInput('');

    try {
      const context = isOverthinking 
        ? `The user is overthinking. Help them break this down into manageable steps and defeat this worry. Be supportive and practical.`
        : `Be a supportive memory companion. Help organize thoughts clearly.`;

      const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'x-api-key': import.meta.env.VITE_ANTHROPIC_API_KEY || '',
          'anthropic-version': '2023-06-01'
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 1000,
          system: context,
          messages: newMessages.slice(-6).map(m => ({ role: m.role, content: m.content }))
        })
      });

      const data = await response.json();
      const aiResponse = data.content ? data.content.map(c => c.text).join('') : 'I apologize, but I encountered an error. Please check your API key configuration.';
      
      const aiMsg = { role: 'assistant', content: aiResponse, timestamp: Date.now() };
      const updatedMessages = [...newMessages, aiMsg];
      setMessages(updatedMessages);

      // Update stats
      let newStats = { ...playerStats, thoughtsSaved: playerStats.thoughtsSaved + 1 };
      newStats = addXP(20, newStats);

      // Create nodes
      const concepts = extractConcepts(input + ' ' + aiResponse);
      const newNodes = [...nodes];
      const newLinks = [...links];
      
      const msgId = `msg-${Date.now()}`;
      const age = 0;
      const health = 100;
      
      newNodes.push({
        id: msgId,
        label: input.slice(0, 30) + '...',
        type: 'thought',
        timestamp: Date.now(),
        fullContent: input,
        age,
        health,
        lastWatered: Date.now()
      });

      concepts.forEach(concept => {
        const existingNode = newNodes.find(n => n.id === concept);
        if (!existingNode) {
          newNodes.push({
            id: concept,
            label: concept,
            type: 'concept',
            timestamp: Date.now(),
            age: 0,
            health: 100,
            lastWatered: Date.now()
          });
        }
        newLinks.push({ source: msgId, target: concept });
        newStats.connectionsCreated++;
      });

      setNodes(newNodes);
      setLinks(newLinks);
      
      const newAchievements = checkAchievements(newStats, achievements);
      setPlayerStats(newStats);
      
      await saveData(updatedMessages, newNodes, newLinks, newStats, newAchievements);
      updateAiMood('supportive');

    } catch (err) {
      console.error('AI Error:', err);
      const errorMsg = { role: 'assistant', content: 'Sorry, I encountered an error. Please make sure your API key is configured correctly.', timestamp: Date.now() };
      setMessages([...newMessages, errorMsg]);
    }

    setLoading(false);
  };

  const defeatBoss = async () => {
    if (!currentBattle) return;

    setLoading(true);
    
    try {
      const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'x-api-key': import.meta.env.VITE_ANTHROPIC_API_KEY || '',
          'anthropic-version': '2023-06-01'
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 1000,
          system: 'Break down this worry into 3 small, actionable steps. Be concise and practical.',
          messages: [{ role: 'user', content: currentBattle.thought }]
        })
      });

      const data = await response.json();
      const solution = data.content ? data.content.map(c => c.text).join('') : 'Break it down into smaller steps, take one at a time, and remember you can handle this!';
      
      const aiMsg = { 
        role: 'assistant', 
        content: `🗡️ BOSS DEFEATED! Here's how to conquer this:\n\n${solution}`, 
        timestamp: Date.now() 
      };
      
      setMessages([...messages, aiMsg]);
      
      let newStats = { 
        ...playerStats, 
        bossesDefeated: playerStats.bossesDefeated + 1,
        thoughtsSaved: playerStats.thoughtsSaved + 1
      };
      newStats = addXP(50, newStats);
      
      const newAchievements = checkAchievements(newStats, achievements);
      setPlayerStats(newStats);
      
      await saveData(messages, nodes, links, newStats, newAchievements);
      
      setCurrentBattle(null);
      updateAiMood('celebrating');
      playSound('achievement');
      
    } catch (err) {
      console.error('Battle error:', err);
      const errorMsg = { 
        role: 'assistant', 
        content: '🗡️ BOSS DEFEATED! Here\'s how to conquer this:\n\n1. Break it into smaller parts\n2. Focus on one thing at a time\n3. Remember that you\'ve overcome challenges before!', 
        timestamp: Date.now() 
      };
      setMessages([...messages, errorMsg]);
      setCurrentBattle(null);
    }
    
    setLoading(false);
  };

  // D3 Visualization with growth animation
  useEffect(() => {
    if (!svgRef.current || nodes.length === 0) return;

    const width = svgRef.current.clientWidth;
    const height = svgRef.current.clientHeight;

    d3.select(svgRef.current).selectAll('*').remove();

    const svg = d3.select(svgRef.current)
      .append('g')
      .attr('transform', `translate(${width/2}, ${height/2})`);

    // Age nodes over time
    const agedNodes = nodes.map(n => {
      const daysSince = (Date.now() - n.lastWatered) / (1000 * 60 * 60 * 24);
      const newHealth = Math.max(0, 100 - (daysSince * 10));
      return { ...n, health: newHealth };
    });

    const simulation = d3.forceSimulation(agedNodes)
      .force('link', d3.forceLink(links).id(d => d.id).distance(100))
      .force('charge', d3.forceManyBody().strength(-300))
      .force('center', d3.forceCenter(0, 0));

    simulationRef.current = simulation;

    const link = svg.append('g')
      .selectAll('line')
      .data(links)
      .enter().append('line')
      .attr('stroke', '#4b5563')
      .attr('stroke-width', 2)
      .attr('opacity', 0.6);

    const node = svg.append('g')
      .selectAll('circle')
      .data(agedNodes)
      .enter().append('circle')
      .attr('r', d => d.type === 'thought' ? 15 : 10)
      .attr('fill', d => {
        if (d.health > 66) return d.type === 'thought' ? '#10b981' : '#8b5cf6';
        if (d.health > 33) return '#f59e0b';
        return '#ef4444';
      })
      .attr('stroke', d => d.health < 50 ? '#fbbf24' : 'none')
      .attr('stroke-width', d => d.health < 50 ? 2 : 0)
      .style('cursor', 'pointer')
      .call(d3.drag()
        .on('start', dragstarted)
        .on('drag', dragged)
        .on('end', dragended))
      .on('click', (event, d) => setSelectedNode(d));

    const label = svg.append('g')
      .selectAll('text')
      .data(agedNodes)
      .enter().append('text')
      .text(d => d.label)
      .attr('font-size', 10)
      .attr('fill', '#e5e7eb')
      .attr('text-anchor', 'middle')
      .attr('dy', 30);

    simulation.on('tick', () => {
      link
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y);

      node
        .attr('cx', d => d.x)
        .attr('cy', d => d.y);

      label
        .attr('x', d => d.x)
        .attr('y', d => d.y);
    });

    function dragstarted(event, d) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }

    function dragged(event, d) {
      d.fx = event.x;
      d.fy = event.y;
    }

    function dragended(event, d) {
      if (!event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }

  }, [nodes, links]);

  if (showSetup) {
    return (
      <div className="h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-gray-900 flex items-center justify-center p-4">
        <div className="bg-gray-800 p-8 rounded-lg max-w-md w-full shadow-2xl border border-purple-500">
          <div className="flex items-center gap-3 mb-6">
            <Lock className="text-purple-400" size={32} />
            <h1 className="text-2xl font-bold text-white">Enter Your Garden</h1>
          </div>
          <p className="text-gray-300 mb-6">
            🌱 Your thoughts grow here. Encrypted. Private. Yours.
          </p>
          <input
            type="password"
            placeholder="Enter password"
            className="w-full p-3 bg-gray-700 text-white rounded mb-4 border border-gray-600 focus:border-purple-500 outline-none"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSetup()}
          />
          <button
            onClick={handleSetup}
            className="w-full bg-gradient-to-r from-purple-600 to-blue-600 text-white p-3 rounded font-semibold hover:from-purple-700 hover:to-blue-700"
          >
            <Key className="inline mr-2" size={18} />
            Unlock Garden
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-gray-900 flex flex-col">
      {/* Stats Bar */}
      <div className="bg-gray-800 border-b border-purple-500 p-3 flex items-center justify-between">
        <div className="flex items-center gap-6">
          <div className="flex items-center gap-2">
            <Star className="text-yellow-400" size={20} />
            <span className="text-white font-bold">Level {playerStats.level}</span>
            <div className="w-32 h-2 bg-gray-700 rounded-full overflow-hidden">
              <div 
                className="h-full bg-gradient-to-r from-yellow-400 to-orange-500"
                style={{ width: `${(playerStats.xp % 100)}%` }}
              />
            </div>
          </div>
          <div className="flex items-center gap-2">
            <Trophy className="text-purple-400" size={20} />
            <span className="text-white">{achievements.length}/{ACHIEVEMENTS.length}</span>
          </div>
          <div className="flex items-center gap-2">
            <Zap className="text-blue-400" size={20} />
            <span className="text-white">{playerStats.streak} day streak</span>
          </div>
          <div className="text-2xl">{getMoodEmoji()}</div>
        </div>
      </div>

      {/* Achievement Popup */}
      {showAchievement && (
        <div className="absolute top-20 left-1/2 transform -translate-x-1/2 bg-gradient-to-r from-yellow-400 to-orange-500 text-white px-6 py-4 rounded-lg shadow-2xl z-50 animate-bounce">
          <div className="flex items-center gap-3">
            <span className="text-3xl">{showAchievement.icon}</span>
            <div>
              <div className="font-bold">{showAchievement.name}</div>
              <div className="text-sm opacity-90">{showAchievement.desc}</div>
            </div>
          </div>
        </div>
      )}

      <div className="flex-1 flex overflow-hidden">
        {/* Chat Panel */}
        <div className="w-1/2 flex flex-col border-r border-purple-500">
          <div className="bg-gray-800 p-4 border-b border-gray-700">
            <div className="flex items-center gap-3">
              <Brain className="text-purple-400" size={28} />
              <div>
                <h1 className="text-xl font-bold text-white">Memory Garden RPG</h1>
                <p className="text-sm text-gray-400">Your AI companion is {aiMood}</p>
              </div>
            </div>
          </div>

          {/* Battle Mode */}
          {currentBattle && (
            <div className="bg-red-900 bg-opacity-50 p-4 border-b border-red-500">
              <div className="flex items-center justify-between mb-3">
                <div className="flex items-center gap-2">
                  <Sword className="text-red-400" />
                  <span className="text-white font-bold">OVERTHINKING BOSS BATTLE</span>
                </div>
                <Heart className="text-red-400" />
              </div>
              <div className="text-white mb-3 italic">"{currentBattle.thought}"</div>
              <button
                onClick={defeatBoss}
                disabled={loading}
                className="w-full bg-red-600 text-white py-2 rounded font-bold hover:bg-red-700 disabled:opacity-50"
              >
                ⚔️ BREAK IT DOWN & DEFEAT
              </button>
            </div>
          )}

          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            {messages.map((msg, i) => (
              <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                <div className={`max-w-[80%] p-3 rounded-lg ${
                  msg.role === 'user' 
                    ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white' 
                    : 'bg-gray-700 text-gray-100'
                }`}>
                  {msg.content}
                </div>
              </div>
            ))}
            {loading && (
              <div className="flex justify-start">
                <div className="bg-gray-700 text-gray-100 p-3 rounded-lg">
                  <Sparkles className="animate-pulse text-purple-400" size={20} />
                </div>
              </div>
            )}
          </div>

          <div className="p-4 bg-gray-800 border-t border-gray-700">
            <div className="flex gap-2">
              <input
                type="text"
                placeholder="Plant a thought..."
                className="flex-1 p-3 bg-gray-700 text-white rounded border border-gray-600 focus:border-purple-500 outline-none"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
              />
              <button
                onClick={sendMessage}
                disabled={loading}
                className="bg-gradient-to-r from-purple-600 to-blue-600 text-white p-3 rounded hover:from-purple-700 hover:to-blue-700 disabled:opacity-50"
              >
                <Send size={20} />
              </button>
            </div>
          </div>
        </div>

        {/* Garden Visualization */}
        <div className="w-1/2 flex flex-col">
          <div className="bg-gray-800 p-4 border-b border-gray-700">
            <h2 className="text-xl font-bold text-white">Your Memory Garden 🌱</h2>
            <p className="text-sm text-gray-400">
              <span className="inline-block w-3 h-3 rounded-full bg-green-500 mr-1"></span>Healthy
              <span className="inline-block w-3 h-3 rounded-full bg-orange-500 ml-3 mr-1"></span>Needs care
              <span className="inline-block w-3 h-3 rounded-full bg-red-500 ml-3 mr-1"></span>Wilting
            </p>
          </div>

          <div className="flex-1 relative">
            <svg ref={svgRef} className="w-full h-full" />
            
            {selectedNode && (
              <div className="absolute top-4 right-4 bg-gray-800 p-4 rounded-lg max-w-xs shadow-lg border border-purple-500">
                <div className="flex items-center justify-between mb-2">
                  <h3 className="text-white font-bold">{selectedNode.type === 'thought' ? '💭 Thought' : '🧠 Concept'}</h3>
                  <button 
                    onClick={() => setSelectedNode(null)}
                    className="text-gray-400 hover:text-white"
                  >
                    ✕
                  </button>
                </div>
                <p className="text-gray-300 text-sm mb-2">{selectedNode.label}</p>
                {selectedNode.fullContent && (
                  <p className="text-gray-400 text-xs mb-2">{selectedNode.fullContent}</p>
                )}
                <div className="flex items-center gap-2">
                  <Heart className="text-red-400" size={16} />
                  <div className="flex-1 h-2 bg-gray-700 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-gradient-to-r from-green-400 to-blue-500"
                      style={{ width: `${selectedNode.health}%` }}
                    />
                  </div>
                  <span className="text-white text-xs">{Math.round(selectedNode.health)}%</span>
                </div>
                <p className="text-gray-500 text-xs mt-2">
                  Planted {new Date(selectedNode.timestamp).toLocaleDateString()}
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default MemoryGardenRPG;
