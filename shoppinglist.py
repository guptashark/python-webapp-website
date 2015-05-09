from handler import Handler

html_form = """
<form>
	<h2>Add a Food</h2>
	<input type="text" name="food">
	<button>Add</button>
</form>
"""

class ShoppingList(Handler):
	def get(self):
		self.write(html_form)
