module.exports = {
  content: [
    "templates/index.html",
    "./templates/**/*.{html,js}",
  ],
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: [
      {
        'mytheme': {

          'primary': '#4506cb',
          'primary-focus': '#2191FB',
          'primary-content': '#ffffff',
          'secondary': '#4506cb',
          'secondary-focus': '#2191FB',
          'secondary-content': '#ffffff',
          'accent': '#2B9720',
          'accent-focus': '#9FFFCB',
          'accent-content': '#ffffff',
          'neutral': '#232528',
          'neutral-focus': '#232528',
          'neutral-content': '#ffffff',
          'base-100': '#0000',

          'base-200': '#232528',
          'base-300': '#EAF6FF',
          'base-content': '#ffffff',
          'info': '#2094f3',
          'success': '#2dd881',
          'warning': '#FFA400',
          'error': '#BB4430',
        },
      },
    ],
  },
}