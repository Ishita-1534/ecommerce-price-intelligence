from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>E-Commerce Store</h1>

        <div class="product">
            <h2>iPhone 16</h2>
            <p class="price">₹79,999</p>
            <p class="rating">4.8</p>
        </div>

        <div class="product">
            <h2>Samsung S25</h2>
            <p class="price">₹74,999</p>
            <p class="rating">4.7</p>
        </div>

    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())