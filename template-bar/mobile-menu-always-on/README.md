# Template bar - Menu hack!

## How to always keep the mobile menu (hamburger menu) even on desktop view

The mobile menu, also called hamburger menu has a great value, specially when you want to hide the navigation bar to not pollute the visibility or readability of your pages.

Here is a little trick/hack to always keep it activated.

- Go to Backoffice -> Look & Feel -> Theme -> Header

Set the breakdown properties to a very high number (like 1 million for example):

```html
<nav class="ods-front-header" ods-responsive-menu breakpoint="1000000">
    <ods-responsive-menu-placeholder>
        <a class="ods-front-header__portal-brand" href="/">
            ##logo##
        </a>
    </ods-responsive-menu-placeholder>
    <ods-responsive-menu-collapsible>
        ...
    </ods-responsive-menu-collapsible>
</nav>
```

- Then, still in the Theme section -> Stylesheet

Add a few CSS properties to remove the header background, to only display the logo on the same background than the overall site:

```css
/* Remove the header background color property to remove the wide banner */
.ods-front-header {
    background-color: inherit;
}
```

Then, add a few colour and size properties to make it more visible:

```css
/* Hamburger menu style : colour and size */
.ods-responsive-menu-placeholder__toggle {
    color: #ff4900;
    opacity: 1;
    font-size: 2.66rem;
}
/* Hamburger menu mouse hover colour! */
.ods-responsive-menu-placeholder__toggle:hover {
    background-color: #2d3f56;
}
```

Save, Apply, and see !

[An example here](https://zapier-odsplus.opendatasoft.com/)