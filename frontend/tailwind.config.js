module.exports = {
  purge: ['./pages/**/*.tsx', './components/*.tsx'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontFamily: {
      sans: ["'Roboto'"],
    },
    extend: {
      colors: {
        dark: '#222',
        primary: '#32325D',
        button: '#042235',
        link: '#556CD6',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}