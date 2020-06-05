const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const CopyPlugin = require('copy-webpack-plugin')

module.exports = {
  mode: 'development',
  entry: {
    app: './src/app.js'
  },
  plugins: [
    new CopyPlugin({
      patterns: [
        { from: 'src/img', to:'img' }
      ]
    }),
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      title: 'ODS Minimal template',
      template: 'public/index.html'
    })
  ],
  devtool: 'inline-source-map',
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  externals: {
    jQuery: 'jquery',
    angular: 'angular',
    ngSanitize: 'angular-sanitize',
    'ods-widgets': 'ods-widgets'
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: [
          'style-loader',
          'css-loader'
        ]
      },
      {
        test: /\.s[ac]ss$/i,
        use: [
          'style-loader',
          'css-loader',
          'sass-loader'
        ]
      }
    ]
  },
  devServer: {
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    port: 9000
  }
}
