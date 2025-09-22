import { test, expect } from '@playwright/test';

test.describe('Home Page', () => {
  test('should display the correct title', async ({ page }) => {
    await page.goto('/');
    
    // Check that the page title is correct
    await expect(page).toHaveTitle('Tailspin Toys - Crowdfunding your new favorite game!');
  });

  test('should display the main heading', async ({ page }) => {
    await page.goto('/');
    
    // Check that the main heading is present - look for the hero heading specifically
    const mainHeading = page.locator('main h1').first();
    await expect(mainHeading).toContainText('Welcome to');
    await expect(mainHeading).toContainText('Tailspin Toys');
  });

  test('should display the welcome message', async ({ page }) => {
    await page.goto('/');
    
    // Check that the welcome message is present - looking for the main subtitle
    const welcomeMessage = page.locator('p').filter({ hasText: 'Discover extraordinary board games' });
    await expect(welcomeMessage).toContainText('Discover extraordinary board games where');
    await expect(welcomeMessage).toContainText('DevOps meets tabletop');
  });
});
