# Task 2 — Read Zomato robots.txt

## Objective
Read Zomato's robots.txt file and explain two rules.

File checked: https://www.zomato.com/robots.txt

## Rule 1

```text
User-agent: Googlebot
Disallow: /admin/
```

**Explanation:** This tells Googlebot not to crawl URLs under the `/admin/` path.

## Rule 2

```text
User-agent: Googlebot
Disallow: /users/
```

**Explanation:** This tells Googlebot not to crawl URLs under the `/users/` path.

## Another rule I noticed

```text
User-agent: *
Disallow: /
```

**Explanation:** The `*` represents the general group of crawlers. `Disallow: /` asks those crawlers not to crawl any path on the site, subject to the applicable robots.txt rules.

## What I learned
robots.txt gives instructions to crawlers about which paths they should or should not crawl. It is not a security mechanism and does not grant permission to access restricted content.

**Note:** Interpret each Disallow line together with its User-agent group because rules can differ between crawlers.
