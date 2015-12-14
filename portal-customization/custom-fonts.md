# Custom fonts

You may want to use fonts other than the *Open Sans* that we are using throughout the platform.

In the following, we'll consider the open-source font *Roboto* that you can download on [google fonts](https://www.google.com/fonts/specimen/Roboto).

This fonts contains 12 styles, that is 6 weights, each available in italic and regular form. For each of these styles, google fonts will provide a `.ttf` file. While most browser support .ttf files, all do not. As a result, you should try to get your fonts files in all of the following formats:

* `.eot` required for Internet Explorer up to version 9.
* `.svg` required for very early version of iOS
* `.ttf` for Safari, android and iOS
* `.woff` for all modern browsers
* `.woff2` for the latest version of browsers

If you are lost with all these formats, a good rule of thumb is to use the `.woff` format since it is supported by all browsers working with the OpenDataSoft platform.

For each of these styles, you'll have to upload the correspondinf files to the platform (using the *Assets* management page) and write the following CSS code.

``` css
@font-face {
  font-family: 'Roboto';
  src: url('/assets/theme_font/<filename>.eot');
  src: url('/assets/theme_font/<filename>.eot?#iefix') format('embedded-opentype'),
       url('/assets/theme_font/<filename>.woff2') format('woff2'),
       url('/assets/theme_font/<filename>.woff') format('woff'),
       url('/assets/theme_font/<filename>.ttf') format('truetype');
  font-style: <normal|italic>;
  font-weight: <100|200|300|400|500|600|700|800|900>;
}
```

Were you to have only the `.woff` format available, you'd write for each style.

``` css
@font-face {
  font-family: 'Roboto';
  src: url('/assets/theme_font/<filename>.woff') format('woff');
  font-style: <normal|italic>;
  font-weight: <100|200|300|400|500|600|700|800|900>;
}
```

With this code set up in the *stylesheet* tab of the *theme* page, we can now use the font within the website.

To replace the *Open Sans* font entirely, you'll only have to write

``` css
html {
  font-family: 'Roboto', Helvetica, arial, sans-serif;
}
```

Note that we're not just writing `font-family: 'Roboto';`. We're also specifying a list of fonts the browser will default to if Roboto was unavailable. The code here specifies that we should use Roboto, and if not available Helvetica, and if not available arial, and in last resort the default sans-serif font of the browser.
