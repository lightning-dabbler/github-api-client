const path = require('path')
const rimraf = require('rimraf')
const UglifyJSPlugin = require('uglifyjs-webpack-plugin')
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');

rimraf.sync('./dist') // Remove dist directory

module.exports = env => (
    {
        mode: env.production ? 'production' : 'development',
        devtool: env.production ? 'source-map' : 'inline-cheap-module-source-map',
        entry: './src/main.js',
        output: {
            path: path.resolve(__dirname, './dist'),
            publicPath: '/',
            sourceMapFilename: `build.[hash].map`,
            filename: `build.[hash].js`
        },
        module: {
            rules: [
                {
                    test: /\.js$/,
                    exclude: /node_modules/,
                    use: {
                        loader: 'babel-loader'
                    }

                },
                {
                    test: /\.vue$/,
                    exclude: /node_modules/,
                    use: {
                        loader: 'vue-loader'
                    }

                },
                {
                    test: /\.css$/,
                    use: ['vue-style-loader', 'style-loader', 'css-loader']
                },
                {
                    test: /\.scss$/,
                    use: [
                        'vue-style-loader',
                        'style-loader',
                        'css-loader',
                        'sass-loader'
                    ]
                }
            ],

        },
        resolve: {
            alias: {
                'vue$': 'vue/dist/vue.common.js',
                '@': path.resolve(__dirname, 'src'),
                views: path.resolve(__dirname, 'src/views'),
                static: path.resolve(__dirname, 'src/static')
            }
        },
        plugins: [
            new HtmlWebpackPlugin({
                filename: 'index.html',
                template: './src/index.html',
                minify: {
                    removeComments: true,
                    minifyJS: true
                }
            }),
            new VueLoaderPlugin(),
            new CopyWebpackPlugin([
                { from: 'src/static/', to: 'static/' },
                { from: 'src/ie.html' }
            ])
        ],
        optimization:
        {
            minimizer:
                [
                    new UglifyJSPlugin({
                        sourceMap: true,
                        uglifyOptions: {
                            output: {
                                comments: false
                            },
                            compress: {
                                drop_console: true
                            }
                        }
                    })
                ]
        },
        devServer: {
            historyApiFallback: true,
            contentBase: 'dist',
            compress: true,
            host: '0.0.0.0',
            port: 8089
        }
    }
);
