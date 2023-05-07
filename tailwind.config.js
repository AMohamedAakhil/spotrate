/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html, js}", "./src/js/*.{html, js}", "./src/components/*.{html,js}"],
  theme: {
    extend: {},
    height: {
      "10v": "10vh",
      "90v": "90vh"
    }
  },
  plugins:  [require("daisyui")],
  daisyui: {
    themes: ["night"],
  },

}

