'''
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.
'''
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # def dp(i):
        #     if i in memo:
        #         return memo[i]
        #     ans=questions[i][0]
        #     for j in range(i):
        #         if i-j>questions[j][1]:
        #             ans=max(ans,dp(j)+questions[i][0])
        #     memo[i]=ans
        #     return memo[i]
        # memo={}
        # res=max(dp(i) for i in range(len(questions)))
        # return res
        def dp(i):
            if i>=len(questions):
                return 0
            if i in memo:
                return memo[i]
            j=i+questions[i][1]+1
            ans=max(questions[i][0]+dp(j),dp(i+1))
            memo[i]=ans
            return memo[i]
        memo={}
        return dp(0)
