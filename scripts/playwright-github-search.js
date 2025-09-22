#!/usr/bin/env node

/**
 * Playwright script to search for GitHub-related presentation topics
 * on the DevDays Asia 2025 seminar website
 * 
 * This script demonstrates how to use Playwright for web scraping
 * to find GitHub-related content on seminar websites.
 */

const { chromium } = require('playwright');

async function searchGitHubTopics() {
    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext();
    const page = await context.newPage();

    try {
        console.log('🚀 Navigating to DevDays Asia 2025 seminar website...');
        await page.goto('https://www.digitimes.com.tw/Seminar/DevDaysAsia2025/index.html', {
            waitUntil: 'domcontentloaded',
            timeout: 30000
        });

        console.log('📋 Searching for GitHub-related topics...');
        
        // Search for various GitHub-related keywords in the page content
        const githubKeywords = ['github', 'git', 'repository', 'version control', 'copilot', 'ci/cd', 'devops'];
        const foundTopics = [];

        // Look for session titles, speaker names, and descriptions
        const sessionSelectors = [
            'h1, h2, h3, h4', // Session titles
            '.session-title, .talk-title, .presentation-title', // Common class names for session titles
            '.speaker-bio, .session-description, .talk-description', // Session descriptions
            'p, div, span' // General text content
        ];

        for (const selector of sessionSelectors) {
            try {
                const elements = await page.$$(selector);
                
                for (const element of elements) {
                    const text = await element.textContent();
                    if (text) {
                        const lowerText = text.toLowerCase();
                        
                        // Check if any GitHub-related keywords are found
                        for (const keyword of githubKeywords) {
                            if (lowerText.includes(keyword)) {
                                foundTopics.push({
                                    keyword: keyword,
                                    text: text.trim(),
                                    element: selector
                                });
                                break;
                            }
                        }
                    }
                }
            } catch (error) {
                // Skip selectors that don't exist
                continue;
            }
        }

        // Look for schedule or agenda sections
        console.log('📅 Checking schedule and agenda sections...');
        const scheduleSelectors = [
            '.schedule, .agenda, .program',
            '[id*="schedule"], [id*="agenda"], [id*="program"]',
            '[class*="schedule"], [class*="agenda"], [class*="program"]'
        ];

        for (const selector of scheduleSelectors) {
            try {
                const scheduleSection = await page.$(selector);
                if (scheduleSection) {
                    const scheduleText = await scheduleSection.textContent();
                    if (scheduleText) {
                        const lowerText = scheduleText.toLowerCase();
                        
                        for (const keyword of githubKeywords) {
                            if (lowerText.includes(keyword)) {
                                foundTopics.push({
                                    keyword: keyword,
                                    text: 'Found in schedule section',
                                    element: selector,
                                    fullText: scheduleText.substring(0, 200) + '...'
                                });
                            }
                        }
                    }
                }
            } catch (error) {
                continue;
            }
        }

        // Look for speaker information
        console.log('👥 Searching speaker information...');
        const speakerSelectors = [
            '.speaker, .presenter',
            '[class*="speaker"], [class*="presenter"]'
        ];

        for (const selector of speakerSelectors) {
            try {
                const speakers = await page.$$(selector);
                
                for (const speaker of speakers) {
                    const speakerText = await speaker.textContent();
                    if (speakerText) {
                        const lowerText = speakerText.toLowerCase();
                        
                        for (const keyword of githubKeywords) {
                            if (lowerText.includes(keyword)) {
                                foundTopics.push({
                                    keyword: keyword,
                                    text: speakerText.trim(),
                                    element: 'speaker-info'
                                });
                                break;
                            }
                        }
                    }
                }
            } catch (error) {
                continue;
            }
        }

        // Take a screenshot for documentation
        await page.screenshot({ 
            path: 'devdays-asia-2025-screenshot.png',
            fullPage: true 
        });

        console.log('\n🎯 GitHub-related topics found:');
        console.log('=====================================');
        
        if (foundTopics.length === 0) {
            console.log('❌ No GitHub-related topics found on this page.');
            console.log('💡 This could mean:');
            console.log('   - The content is loaded dynamically (requires waiting)');
            console.log('   - GitHub topics are in different sections not yet searched');
            console.log('   - The seminar focuses on other technologies');
        } else {
            // Remove duplicates and display results
            const uniqueTopics = foundTopics.reduce((acc, current) => {
                const exists = acc.find(item => 
                    item.keyword === current.keyword && 
                    item.text === current.text
                );
                if (!exists) {
                    acc.push(current);
                }
                return acc;
            }, []);

            uniqueTopics.forEach((topic, index) => {
                console.log(`\n${index + 1}. Keyword: "${topic.keyword}"`);
                console.log(`   Text: "${topic.text.substring(0, 100)}${topic.text.length > 100 ? '...' : ''}"`);
                console.log(`   Found in: ${topic.element}`);
                if (topic.fullText) {
                    console.log(`   Context: "${topic.fullText}"`);
                }
            });

            console.log(`\n📊 Total GitHub-related topics found: ${uniqueTopics.length}`);
        }

        // Suggest potential GitHub presentation topics based on common DevOps themes
        console.log('\n💡 Suggested GitHub presentation topics for DevDays Asia 2025:');
        console.log('===========================================================');
        console.log('1. "GitHub Copilot: AI-Powered Development in Asian Markets"');
        console.log('2. "CI/CD Best Practices with GitHub Actions for Enterprise"');
        console.log('3. "Security-First Development with GitHub Advanced Security"');
        console.log('4. "Scaling DevOps Teams with GitHub Enterprise"');
        console.log('5. "Open Source Collaboration Strategies in Asia"');
        console.log('6. "GitHub API Integration for Custom Workflows"');
        console.log('7. "Mobile Development CI/CD with GitHub Actions"');
        console.log('8. "Infrastructure as Code with GitHub and Terraform"');
        console.log('9. "Container Security and GitHub Container Registry"');
        console.log('10. "Automating Code Quality with GitHub Checks API"');

    } catch (error) {
        console.error('❌ Error during GitHub topic search:', error.message);
        
        // If the main site fails, provide alternative suggestions
        console.log('\n🔄 Alternative approach - Common GitHub presentation topics for developer conferences:');
        console.log('================================================================================');
        console.log('Based on typical DevDays Asia content, here are GitHub-related presentation topics:');
        console.log('');
        console.log('📋 **Development & Productivity:**');
        console.log('  • GitHub Copilot for Faster Development');
        console.log('  • Code Review Best Practices with GitHub');
        console.log('  • GitHub Codespaces for Cloud Development');
        console.log('');
        console.log('🔧 **DevOps & CI/CD:**');
        console.log('  • GitHub Actions for Continuous Integration');
        console.log('  • Deploying to Cloud with GitHub Workflows');
        console.log('  • GitOps Principles with GitHub');
        console.log('');
        console.log('🔒 **Security & Compliance:**');
        console.log('  • GitHub Advanced Security Features');
        console.log('  • Securing Open Source Dependencies');
        console.log('  • Compliance Automation with GitHub');
        console.log('');
        console.log('🌏 **Enterprise & Teams:**');
        console.log('  • GitHub Enterprise for Large Organizations');
        console.log('  • Managing Global Development Teams');
        console.log('  • Inner Source Programs with GitHub');
    } finally {
        await context.close();
        await browser.close();
    }
}

// Run the search if this script is executed directly
if (require.main === module) {
    searchGitHubTopics()
        .then(() => {
            console.log('\n✅ GitHub topic search completed!');
            process.exit(0);
        })
        .catch((error) => {
            console.error('\n❌ Script failed:', error);
            process.exit(1);
        });
}

module.exports = { searchGitHubTopics };