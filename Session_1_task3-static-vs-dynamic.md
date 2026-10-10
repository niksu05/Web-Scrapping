# Task 3 — Compare Myntra and Instagram Content Loading

## Objective
Compare how page content loads on Myntra and Instagram using browser Developer Tools.

## Observation

**Myntra:** More of the page's initial content appears to be delivered when the page first loads. The website may still make extra requests for data and other resources.

**Instagram:** Much of the feed content is fetched dynamically through JavaScript and network/API requests after the page begins loading. Therefore, downloading only the initial HTML may not include all the posts visible in the browser.

## Key difference
The main difference is how much useful content is present in the initial HTML response. Dynamic pages may need JavaScript execution or additional network requests to display more content.

## What I learned
The content visible in a browser is not always all present in the first HTML response. The Network tab helps me observe extra requests made while a page loads.

## Evidence
Add screenshots of your page or DevTools observations to the `screenshots/` folder.
