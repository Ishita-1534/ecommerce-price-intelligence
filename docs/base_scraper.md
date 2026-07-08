# Base Scraper

## Purpose

The `BaseScraper` class is responsible for launching the Chrome browser using Selenium, navigating through web pages, and retrieving the HTML source for further parsing.

## Responsibilities

- Initialize the Selenium WebDriver
- Open the target webpage
- Retrieve the page source
- Close the browser session

## Methods

### `get_page(url)`

Navigates to the specified URL and returns the HTML source of the webpage.

### `close()`

Closes the browser and ends the Selenium session.

## Status

Completed