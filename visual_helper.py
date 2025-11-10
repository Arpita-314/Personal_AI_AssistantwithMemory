"""
Visual Helper Module
Provides visual learning aids including charts, diagrams, and text-to-image generation.
"""

import os
from typing import List, Dict, Optional
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime
import numpy as np


class VisualHelper:
    """Provides visual learning aids and representations."""
    
    def __init__(self, output_dir: str = "visualizations"):
        """
        Initialize the Visual Helper.
        
        Args:
            output_dir: Directory to save generated visualizations
        """
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def create_concept_map(self, concepts: Dict[str, List[str]], title: str = "Concept Map") -> str:
        """
        Create a simple concept map visualization.
        
        Args:
            concepts: Dictionary mapping main concepts to related sub-concepts
            title: Title for the concept map
            
        Returns:
            Path to the saved image
        """
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        
        # Central concept
        main_concepts = list(concepts.keys())
        if not main_concepts:
            return ""
        
        # Layout concepts in a circular pattern
        num_concepts = len(main_concepts)
        angles = np.linspace(0, 2 * np.pi, num_concepts, endpoint=False)
        
        center_x, center_y = 5, 5
        radius = 3
        
        for i, (concept, sub_concepts) in enumerate(concepts.items()):
            # Position main concept
            x = center_x + radius * np.cos(angles[i])
            y = center_y + radius * np.sin(angles[i])
            
            # Draw main concept
            circle = mpatches.Circle((x, y), 0.5, color='lightblue', ec='darkblue', linewidth=2)
            ax.add_patch(circle)
            ax.text(x, y, concept[:15], ha='center', va='center', fontsize=10, fontweight='bold')
            
            # Draw line to center
            ax.plot([center_x, x], [center_y, y], 'k--', alpha=0.3)
            
            # Draw sub-concepts
            if sub_concepts:
                sub_radius = 1.2
                sub_angles = np.linspace(0, 2 * np.pi, len(sub_concepts), endpoint=False)
                
                for j, sub_concept in enumerate(sub_concepts[:5]):  # Limit to 5 sub-concepts
                    sub_x = x + sub_radius * np.cos(sub_angles[j])
                    sub_y = y + sub_radius * np.sin(sub_angles[j])
                    
                    # Draw sub-concept
                    rect = mpatches.Rectangle((sub_x - 0.3, sub_y - 0.2), 0.6, 0.4, 
                                              color='lightgreen', ec='darkgreen', linewidth=1)
                    ax.add_patch(rect)
                    ax.text(sub_x, sub_y, sub_concept[:10], ha='center', va='center', fontsize=8)
                    
                    # Draw connection line
                    ax.plot([x, sub_x], [y, sub_y], 'g-', alpha=0.5, linewidth=1)
        
        # Add center title
        center_circle = mpatches.Circle((center_x, center_y), 0.6, color='lightyellow', 
                                       ec='orange', linewidth=2)
        ax.add_patch(center_circle)
        ax.text(center_x, center_y, 'Main\nTopic', ha='center', va='center', 
               fontsize=11, fontweight='bold')
        
        filename = f"concept_map_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_timeline(self, events: List[Dict[str, str]], title: str = "Timeline") -> str:
        """
        Create a timeline visualization.
        
        Args:
            events: List of event dictionaries with 'date' and 'description' keys
            title: Title for the timeline
            
        Returns:
            Path to the saved image
        """
        if not events:
            return ""
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Sort events by date if possible
        sorted_events = sorted(events, key=lambda x: x.get('date', ''))
        
        y_pos = 0.5
        for i, event in enumerate(sorted_events[:10]):  # Limit to 10 events
            x_pos = i / max(len(sorted_events) - 1, 1)
            
            # Alternate positions
            y_offset = 0.2 if i % 2 == 0 else -0.2
            
            # Draw point
            ax.plot(x_pos, y_pos, 'o', markersize=10, color='blue')
            
            # Draw line to text
            ax.plot([x_pos, x_pos], [y_pos, y_pos + y_offset], 'k--', alpha=0.3)
            
            # Add text
            date_text = event.get('date', f'Event {i+1}')
            desc_text = event.get('description', '')[:30]
            ax.text(x_pos, y_pos + y_offset, f"{date_text}\n{desc_text}", 
                   ha='center', va='bottom' if y_offset > 0 else 'top',
                   fontsize=9, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # Draw main timeline
        ax.axhline(y=y_pos, color='gray', linewidth=2)
        
        ax.set_xlim(-0.1, 1.1)
        ax.set_ylim(-0.5, 1.5)
        ax.axis('off')
        ax.set_title(title, fontsize=14, fontweight='bold')
        
        filename = f"timeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_bar_chart(self, data: Dict[str, float], title: str = "Bar Chart", 
                        xlabel: str = "Categories", ylabel: str = "Values") -> str:
        """
        Create a bar chart visualization.
        
        Args:
            data: Dictionary mapping labels to values
            title: Chart title
            xlabel: X-axis label
            ylabel: Y-axis label
            
        Returns:
            Path to the saved image
        """
        if not data:
            return ""
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        labels = list(data.keys())
        values = list(data.values())
        colors = plt.cm.viridis(np.linspace(0, 1, len(labels)))
        
        bars = ax.bar(labels, values, color=colors)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}',
                   ha='center', va='bottom', fontsize=10)
        
        ax.set_xlabel(xlabel, fontsize=12)
        ax.set_ylabel(ylabel, fontsize=12)
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        
        plt.xticks(rotation=45, ha='right')
        
        filename = f"bar_chart_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_mind_map(self, central_idea: str, branches: Dict[str, List[str]], 
                       title: str = "Mind Map") -> str:
        """
        Create a mind map visualization.
        
        Args:
            central_idea: The central concept
            branches: Dictionary mapping branch names to sub-items
            title: Title for the mind map
            
        Returns:
            Path to the saved image
        """
        fig, ax = plt.subplots(figsize=(14, 10))
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.axis('off')
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        
        # Draw central idea
        center = mpatches.Circle((0, 0), 0.8, color='gold', ec='orange', linewidth=3)
        ax.add_patch(center)
        ax.text(0, 0, central_idea[:20], ha='center', va='center', 
               fontsize=12, fontweight='bold')
        
        # Draw branches
        num_branches = len(branches)
        if num_branches == 0:
            return ""
        
        angles = np.linspace(0, 2 * np.pi, num_branches, endpoint=False)
        colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 
                 'lightpink', 'lightgray', 'lavender', 'peachpuff']
        
        for i, (branch_name, items) in enumerate(branches.items()):
            angle = angles[i]
            branch_x = 3 * np.cos(angle)
            branch_y = 3 * np.sin(angle)
            
            # Draw branch node
            color = colors[i % len(colors)]
            branch_circle = mpatches.Circle((branch_x, branch_y), 0.6, 
                                           color=color, ec='darkblue', linewidth=2)
            ax.add_patch(branch_circle)
            ax.text(branch_x, branch_y, branch_name[:15], ha='center', va='center', 
                   fontsize=10, fontweight='bold')
            
            # Draw line to center
            ax.plot([0, branch_x], [0, branch_y], 'k-', linewidth=2, alpha=0.5)
            
            # Draw sub-items
            for j, item in enumerate(items[:4]):  # Limit to 4 items per branch
                angle_offset = (j - 1.5) * 0.3
                item_angle = angle + angle_offset
                item_x = branch_x + 1.2 * np.cos(item_angle)
                item_y = branch_y + 1.2 * np.sin(item_angle)
                
                # Draw item box
                ax.add_patch(mpatches.Rectangle((item_x - 0.4, item_y - 0.2), 0.8, 0.4,
                                                color='white', ec='gray', linewidth=1))
                ax.text(item_x, item_y, item[:12], ha='center', va='center', fontsize=8)
                
                # Draw connecting line
                ax.plot([branch_x, item_x], [branch_y, item_y], 'gray', 
                       linewidth=1, alpha=0.5)
        
        filename = f"mind_map_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_flowchart(self, steps: List[str], title: str = "Process Flowchart") -> str:
        """
        Create a simple flowchart visualization.
        
        Args:
            steps: List of process steps
            title: Title for the flowchart
            
        Returns:
            Path to the saved image
        """
        if not steps:
            return ""
        
        fig, ax = plt.subplots(figsize=(8, 2 + len(steps)))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, len(steps) + 1)
        ax.axis('off')
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        
        x_center = 5
        
        for i, step in enumerate(steps):
            y_pos = len(steps) - i
            
            # Draw box
            rect = mpatches.FancyBboxPatch((x_center - 2, y_pos - 0.3), 4, 0.6,
                                          boxstyle="round,pad=0.1", 
                                          facecolor='lightblue', 
                                          edgecolor='darkblue', linewidth=2)
            ax.add_patch(rect)
            
            # Add step text
            ax.text(x_center, y_pos, f"{i+1}. {step[:30]}", 
                   ha='center', va='center', fontsize=10, fontweight='bold')
            
            # Draw arrow to next step
            if i < len(steps) - 1:
                ax.annotate('', xy=(x_center, y_pos - 0.5), 
                          xytext=(x_center, y_pos - 0.3),
                          arrowprops=dict(arrowstyle='->', lw=2, color='black'))
        
        filename = f"flowchart_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
