import { defineConfig } from 'astro/config';
import tailwind from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://vpstier.com',
  vite: {
    plugins: [tailwind()],
  },
  integrations: [sitemap()],
  output: 'static',
});
