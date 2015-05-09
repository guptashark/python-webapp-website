from handler import Handler

hidden_html = """
<input type="hidden" name="food" value="%s">
"""

item_html = "<li>%s</li>"

shopping_list_html = """
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""

class ShoppingList(Handler):
	def get(self):
		myItems = self.request.get_all("food")
		self.render("shoppinglist.html", items = myItems)
