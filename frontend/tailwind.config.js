/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        dark: '#36393f',
        darker: '#2f3136',
        primary: '#5865f2',
        success: '#43b581',
        danger: '#f04747',
      },
    },
  },
  plugins: [],
};
