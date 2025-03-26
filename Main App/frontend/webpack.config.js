const path = require("path");

module.exports = {
    module: {
        rules: [
          {
            test: /\.js$/,
            include: [
              path.resolve(__dirname, "src"),
              path.resolve(__dirname, "node_modules/journey-experience")  // ✅ Force Babel to process this package
            ],
            use: {
              loader: "babel-loader",
              options: {
                presets: ["@babel/preset-env", "@babel/preset-react"]
              }
            }
          }
        ]
      }      
};
