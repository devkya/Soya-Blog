const { defineConfig } = require('@vue/cli-service');
module.exports = defineConfig({
	transpileDependencies: ['vuetify'],

	outputDir: 'dist', // default : 'dist'
	publicPath: '/', // default : '/'
	assetsDir: 'static',

	devServer: {
		proxy: 'http://localhost:8000',
	},
});
