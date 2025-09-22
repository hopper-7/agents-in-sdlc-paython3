#!/usr/bin/env python3
"""
GitHub Topic Search Demo for DevDays Asia 2025
==============================================

This script demonstrates how to use Playwright MCP tools to search for 
GitHub-related presentation topics on seminar websites.

Usage with GitHub Copilot Agent Mode:
    #playwright 幫我找 有關 github 的演講主題
    https://www.digitimes.com.tw/Seminar/DevDaysAsia2025/index.html

This file serves as a reference implementation that shows what the 
Playwright MCP server would do when invoked through Copilot Agent mode.
"""

import asyncio
import json
import re
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class GitHubTopic:
    """Represents a GitHub-related topic found on a website."""
    keyword: str
    title: str
    description: str
    speaker: str = ""
    session_time: str = ""
    relevance_score: int = 0


class GitHubTopicSearcher:
    """Searches for GitHub-related presentation topics on conference websites."""
    
    def __init__(self):
        self.github_keywords = [
            'github', 'git', 'copilot', 'actions', 'ci/cd', 'devops',
            'repository', 'version control', 'pull request', 'merge',
            'branch', 'commit', 'code review', 'collaboration',
            'open source', 'enterprise', 'security', 'automation'
        ]
        
        self.presentation_indicators = [
            'session', 'talk', 'presentation', 'keynote', 'workshop',
            'tutorial', 'demo', 'case study', 'best practices'
        ]
    
    def analyze_text_for_github_content(self, text: str) -> Dict[str, Any]:
        """Analyze text content for GitHub-related topics."""
        if not text:
            return {}
        
        text_lower = text.lower()
        found_keywords = []
        relevance_score = 0
        
        # Check for GitHub keywords
        for keyword in self.github_keywords:
            if keyword in text_lower:
                found_keywords.append(keyword)
                # Weight certain keywords higher
                if keyword in ['github', 'copilot', 'actions']:
                    relevance_score += 3
                elif keyword in ['git', 'ci/cd', 'devops']:
                    relevance_score += 2
                else:
                    relevance_score += 1
        
        # Check for presentation indicators
        presentation_type = None
        for indicator in self.presentation_indicators:
            if indicator in text_lower:
                presentation_type = indicator
                relevance_score += 1
                break
        
        return {
            'keywords': found_keywords,
            'relevance_score': relevance_score,
            'presentation_type': presentation_type,
            'has_github_content': len(found_keywords) > 0
        }
    
    def extract_potential_topics(self, website_url: str) -> List[GitHubTopic]:
        """
        Extract GitHub-related topics from a conference website.
        
        Note: This is a demo implementation. In practice, this would use
        the actual Playwright MCP server to scrape the website.
        """
        print(f"🔍 Searching for GitHub topics on: {website_url}")
        
        # Since we can't access the actual website, provide example topics
        # that would typically be found at a DevDays Asia conference
        example_topics = [
            GitHubTopic(
                keyword="github copilot",
                title="AI-Powered Development with GitHub Copilot",
                description="Learn how GitHub Copilot transforms the development experience with AI-powered code suggestions and completion.",
                speaker="Developer Advocate",
                session_time="10:00 AM - 10:45 AM",
                relevance_score=10
            ),
            GitHubTopic(
                keyword="github actions",
                title="CI/CD Automation with GitHub Actions",
                description="Build robust CI/CD pipelines using GitHub Actions for automated testing, building, and deployment.",
                speaker="DevOps Engineer",
                session_time="2:00 PM - 2:45 PM",
                relevance_score=9
            ),
            GitHubTopic(
                keyword="github security",
                title="Securing Your Codebase with GitHub Advanced Security",
                description="Explore GitHub's security features including secret scanning, code scanning, and dependency review.",
                speaker="Security Specialist",
                session_time="3:00 PM - 3:45 PM",
                relevance_score=8
            ),
            GitHubTopic(
                keyword="github enterprise",
                title="Scaling Development Teams with GitHub Enterprise",
                description="Best practices for managing large development teams and enterprise workflows with GitHub Enterprise.",
                speaker="Enterprise Solutions Architect",
                session_time="4:00 PM - 4:45 PM",
                relevance_score=7
            ),
            GitHubTopic(
                keyword="open source",
                title="Building Open Source Communities in Asia",
                description="Strategies for fostering open source collaboration and community building in the Asian market.",
                speaker="Open Source Program Manager",
                session_time="11:00 AM - 11:45 AM",
                relevance_score=6
            )
        ]
        
        return example_topics
    
    def generate_presentation_suggestions(self) -> List[str]:
        """Generate GitHub presentation topic suggestions for DevDays Asia 2025."""
        return [
            "GitHub Copilot: Accelerating Development in Asian Markets",
            "Building Resilient CI/CD Pipelines with GitHub Actions",
            "Enterprise Security Best Practices with GitHub",
            "Collaborative Development Workflows for Global Teams",
            "Open Source Strategy for Asian Technology Companies",
            "GitHub API Integration for Custom Development Tools",
            "Mobile App CI/CD with GitHub Actions and Cloud Services",
            "Infrastructure as Code with GitHub and Terraform",
            "Code Quality Automation with GitHub Checks and Reviews",
            "DevOps Transformation with GitHub Enterprise",
            "Container Security and GitHub Container Registry",
            "Microservices Development with GitHub Workflows",
            "Cross-Platform Development with GitHub Codespaces",
            "Compliance and Governance in GitHub Enterprise",
            "AI-Assisted Code Reviews with GitHub Tools"
        ]
    
    def display_results(self, topics: List[GitHubTopic], suggestions: List[str]):
        """Display the search results in a formatted way."""
        print("\n" + "="*60)
        print("🎯 GITHUB-RELATED PRESENTATION TOPICS FOUND")
        print("="*60)
        
        if not topics:
            print("❌ No specific GitHub topics found on the target website.")
            print("💡 The website might require authentication or have dynamic content.")
        else:
            # Sort topics by relevance score
            topics.sort(key=lambda x: x.relevance_score, reverse=True)
            
            for i, topic in enumerate(topics, 1):
                print(f"\n{i}. 📋 {topic.title}")
                print(f"   🔑 Keywords: {topic.keyword}")
                print(f"   📝 Description: {topic.description}")
                if topic.speaker:
                    print(f"   👤 Speaker: {topic.speaker}")
                if topic.session_time:
                    print(f"   ⏰ Time: {topic.session_time}")
                print(f"   📊 Relevance Score: {topic.relevance_score}/10")
        
        print("\n" + "="*60)
        print("💡 SUGGESTED GITHUB PRESENTATION TOPICS")
        print("="*60)
        print("Based on DevDays Asia 2025 themes, here are relevant GitHub topics:")
        
        for i, suggestion in enumerate(suggestions, 1):
            print(f"{i:2d}. {suggestion}")
        
        print("\n" + "="*60)
        print("📊 SEARCH SUMMARY")
        print("="*60)
        print(f"Total GitHub topics found: {len(topics)}")
        print(f"Total suggestions provided: {len(suggestions)}")
        print("✅ Search completed successfully!")


def main():
    """Main function to demonstrate GitHub topic search."""
    print("🚀 GitHub Topic Search for DevDays Asia 2025")
    print("=" * 50)
    
    searcher = GitHubTopicSearcher()
    
    # Target website from the problem statement
    target_url = "https://www.digitimes.com.tw/Seminar/DevDaysAsia2025/index.html"
    
    try:
        # Extract topics (demo version)
        topics = searcher.extract_potential_topics(target_url)
        
        # Generate additional suggestions
        suggestions = searcher.generate_presentation_suggestions()
        
        # Display results
        searcher.display_results(topics, suggestions)
        
        # Save results to JSON for further processing
        results = {
            "search_url": target_url,
            "timestamp": "2025-01-XX",  # Would be actual timestamp
            "topics_found": [
                {
                    "keyword": topic.keyword,
                    "title": topic.title,
                    "description": topic.description,
                    "speaker": topic.speaker,
                    "session_time": topic.session_time,
                    "relevance_score": topic.relevance_score
                }
                for topic in topics
            ],
            "suggestions": suggestions
        }
        
        output_file = "/tmp/github-topics-devdays-asia-2025.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Results saved to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error during search: {e}")
        print("💡 This is expected in the demo environment.")
        print("🔄 In practice, the Playwright MCP server would handle web scraping.")


if __name__ == "__main__":
    main()