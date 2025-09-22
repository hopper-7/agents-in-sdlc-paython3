/**
 * Svelte configuration for the Tailspin Toys Crowd Funding platform.
 * Configures preprocessing for Svelte components used within Astro pages.
 */
import { vitePreprocess } from '@astrojs/svelte';

export default {
	preprocess: vitePreprocess(),
}
