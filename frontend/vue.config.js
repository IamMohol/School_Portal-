const BundleTracker = require("webpack-bundle-tracker");
const webpack = require('webpack');
module.exports = {
    baseUrl: "http://0.0.0.0:8080/",
    outputDir: './dist/',
    // configureWebpack:{
    //   plugins:[
    //       new webpack.ProvidePlugin({
    //         axios: 'axios',
    //         'window.axios': 'axios'
    //     }),
    //   ]
    // },
    chainWebpack: config => {

        config.optimization
            .splitChunks(false)

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: '../frontend/webpack-stats.json'}]);

        config
            .plugin('provide')
            .use(webpack.ProvidePlugin,[{
                $:'axios',
                axios: 'axios',
                'window.axios': 'axios'
            }]);

        config.resolve.alias
            .set('__STATIC__', 'static')

        config.devServer
            .public('http://0.0.0.0:8080')
            .host('0.0.0.0')
            .port(8080)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .headers({"Access-Control-Allow-Origin": ["\*"]})
            }
        };