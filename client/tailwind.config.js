/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    colors: {
      'soft-gray': '#D4D4D4',
      'light-green-gray': '#B7B7A4',
      'dark-green-gray': '#283618',
      'off-white': '#F0EFEB',
    },
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
  },
  plugins: [],
}

