class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
    
        valid_parentheses = ['()']

        for _ in range(n-1):
            new_valid_parentheses = set()
            for parantheses in valid_parentheses:
                for i in range(len(parantheses)):
                    new_valid_parentheses.add(parantheses[:i] + '()' + parantheses[i:])
            valid_parentheses = new_valid_parentheses
        return valid_parentheses