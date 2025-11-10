"""
AI Assistant module for generating hints and solutions
"""
from typing import List, Dict, Tuple
import openai
from anthropic import Anthropic

class AIAssistant:
    """Handles AI interactions for generating hints and solutions"""
    
    def __init__(self, provider: str, api_key: str, model: str):
        self.provider = provider.lower()
        self.model = model
        
        if self.provider == 'openai':
            openai.api_key = api_key
            self.client = openai.OpenAI(api_key=api_key)
        elif self.provider == 'anthropic':
            self.client = Anthropic(api_key=api_key)
        else:
            raise ValueError(f"Unsupported AI provider: {provider}")
    
    def analyze_question(self, question: str, language: str = 'python') -> Dict[str, any]:
        """
        Analyze a coding question and generate hints and solution
        
        Args:
            question: The coding question text
            language: Target programming language
            
        Returns:
            Dictionary with hints, solution, complexity, and difficulty
        """
        prompt = self._create_analysis_prompt(question, language)
        
        if self.provider == 'openai':
            response = self._call_openai(prompt)
        else:
            response = self._call_anthropic(prompt)
        
        return self._parse_response(response)
    
    def _create_analysis_prompt(self, question: str, language: str) -> str:
        """Create prompt for analyzing coding question"""
        return f"""Analyze the following coding interview question and provide:
1. Three progressive hints (from subtle to more revealing)
2. A complete solution in {language}
3. Time and space complexity
4. Difficulty level (Easy/Medium/Hard)

Question:
{question}

Respond in the following format:
HINTS:
1. [First hint - subtle]
2. [Second hint - moderate]
3. [Third hint - revealing]

SOLUTION:
```{language}
[Complete solution code]
```

COMPLEXITY:
Time: [time complexity]
Space: [space complexity]

DIFFICULTY: [Easy/Medium/Hard]

EXPLANATION:
[Brief explanation of the approach]
"""
    
    def _call_openai(self, prompt: str) -> str:
        """Call OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert coding interview assistant. Provide clear, concise hints and solutions."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error calling OpenAI: {str(e)}"
    
    def _call_anthropic(self, prompt: str) -> str:
        """Call Anthropic API"""
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error calling Anthropic: {str(e)}"
    
    def _parse_response(self, response: str) -> Dict[str, any]:
        """Parse AI response into structured format"""
        result = {
            'hints': [],
            'solution': '',
            'complexity': {'time': '', 'space': ''},
            'difficulty': 'Unknown',
            'explanation': ''
        }
        
        try:
            lines = response.split('\n')
            current_section = None
            solution_lines = []
            in_code_block = False
            
            for line in lines:
                line_strip = line.strip()
                
                if line_strip.startswith('HINTS:'):
                    current_section = 'hints'
                elif line_strip.startswith('SOLUTION:'):
                    current_section = 'solution'
                elif line_strip.startswith('COMPLEXITY:'):
                    current_section = 'complexity'
                elif line_strip.startswith('DIFFICULTY:'):
                    current_section = 'difficulty'
                    result['difficulty'] = line_strip.replace('DIFFICULTY:', '').strip()
                elif line_strip.startswith('EXPLANATION:'):
                    current_section = 'explanation'
                elif current_section == 'hints' and (line_strip.startswith('1.') or 
                                                      line_strip.startswith('2.') or 
                                                      line_strip.startswith('3.')):
                    result['hints'].append(line_strip[2:].strip())
                elif current_section == 'solution':
                    if '```' in line:
                        in_code_block = not in_code_block
                    elif in_code_block:
                        solution_lines.append(line)
                elif current_section == 'complexity':
                    if 'Time:' in line:
                        result['complexity']['time'] = line.split('Time:')[1].strip()
                    elif 'Space:' in line:
                        result['complexity']['space'] = line.split('Space:')[1].strip()
                elif current_section == 'explanation' and line_strip:
                    result['explanation'] += line_strip + ' '
            
            result['solution'] = '\n'.join(solution_lines)
            result['explanation'] = result['explanation'].strip()
            
        except Exception as e:
            # If parsing fails, return raw response
            result['explanation'] = response
        
        return result
    
    def get_quick_hint(self, question: str) -> str:
        """Get a quick hint for a question"""
        prompt = f"Provide one subtle hint for this coding problem: {question}"
        
        if self.provider == 'openai':
            response = self._call_openai(prompt)
        else:
            response = self._call_anthropic(prompt)
        
        return response
