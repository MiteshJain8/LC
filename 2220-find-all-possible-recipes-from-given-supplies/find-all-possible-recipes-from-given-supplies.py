class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def dfs(r):
            if r in can_cook:
                return can_cook[r]
            if r not in recipe_idx:
                return False
            can_cook[r] = False

            for nei in ingredients[recipe_idx[r]]:
                if not dfs(nei):
                    return False
            
            can_cook[r] = True
            return can_cook[r]

        can_cook = {s: True for s in supplies}
        recipe_idx = {r:i for i,r in enumerate(recipes)}
        return [r for r in recipes if dfs(r)]