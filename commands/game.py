import discord
from discord.ext import commands
from Core.classes import Cog_Extension
import random

class Game(Cog_Extension):

    @commands.command()
    async def guess(self, ctx): 
        mode = ""
        await ctx.send("請選擇遊戲難度並發送留言，目前可選擇 easy 或 hard")
        mode = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
        #定義一個 lambda 函式作為 check 的參數，以確定哪些訊息可以觸發指令
        
        async def play_easy(self, ctx):
            print("Entered play_easy or play_hard function")
            secret_number = random.randint(1, 100)  #用randint隨機選擇整數
            await ctx.send("歡迎遊玩猜數字遊戲owo 請猜一個1~100內的正整數") #ctx.send() 可將回應傳送到指令所在的頻道，而不是使用 print() 函數顯示在控制台     
            low , high =1 , 100
            count = 0  # 每次開始遊戲時重置猜測次數為 0
            while True: #建立無窮迴圈直到玩家猜出答案
                guess = await ctx.bot.wait_for("message", check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

                if guess.content == "finish": # 使用 guess.content 可以獲取到使用者輸入的內容
                    await ctx.send(f"{ctx.author.mention} 已離開遊戲QwQ 歡迎下次再來owo")
                    break
                try:                
                    guess = int(guess.content) 
                except ValueError:
                    await ctx.send("請輸入一個整數。")
                    continue
                # try-except 敘述可以讓程式在遇到錯誤時不會直接終止

                if guess < low or guess > high:                
                    await ctx.send("你猜的數字超出範圍了0.0")
                    continue

                if guess == secret_number:            
                    await ctx.send(f"恭喜你猜對了！答案是 {secret_number}，你總共猜了 {count+1} 次") # 
                    # {字串格式化}能解決參數類型錯誤:TypeError: Context.send() takes from 1 to 2 positional arguments but 3 were given
                    break  #玩家猜對了，遊戲結束

                elif guess < secret_number:            
                    await ctx.send("你猜的數字太小了，請繼續猜測！範圍是 {}~{}".format(guess+1, high))
                    low = guess+1
                    count += 1
                    
                else:
                    await ctx.send("你猜的數字太大了，請繼續猜測！範圍是 {}~{}".format(low, guess-1))
                    high = guess-1
                    count += 1

        async def play_hard(self, ctx):
            print("Entered play_easy or play_hard function")
            secret_number = random.randint(1, 100)
            await ctx.send("歡迎遊玩猜數字遊戲owo 請猜一個1~100內的正整數,挑戰模式僅有五次猜測機會")
            low , high =1 , 100
            count = 1
            while count <= 5: 
                guess = await ctx.bot.wait_for("message", check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

                if guess.content == "finish": 
                    await ctx.send(f"{ctx.author.mention} 已離開遊戲QwQ 歡迎下次再來owo")
                    break
                try:                
                    guess = int(guess.content) 
                except ValueError:
                    await ctx.send("請輸入一個整數。")
                    continue

                if guess < low or guess > high:                
                    await ctx.send("你猜的數字超出範圍了0.0")
                    continue

                if guess == secret_number:            
                    await ctx.send(f"恭喜你猜對了！答案是 {secret_number}，你總共猜了 {count} 次") 
                    break 

                elif guess < secret_number:            
                    await ctx.send("你猜的數字太小了，請繼續猜測！範圍是 {}~{}".format(guess+1, high))
                    low = guess+1
                    count += 1
                    
                else:
                    await ctx.send("你猜的數字太大了，請繼續猜測！範圍是 {}~{}".format(low, guess-1))
                    high = guess-1
                    count += 1

                if count > 5:
                    await ctx.send(f"本次挑戰失敗，正確答案是 {secret_number} ,歡迎下次再來_._")
                    break
        
        if mode.content.lower() == "easy":
            await ctx.send("遊戲難度設定為easy")
            print("Entered play_easy function")
            await play_easy(self, ctx)
        elif mode.content.lower() == "hard":
            await ctx.send("遊戲難度設定為hard")
            print("Entered play_hard function")
            await play_hard(self, ctx)
        else:
            await ctx.send("無效的難度選擇,請輸入easy或hard")

    @guess.error
    async def guess_error(self, ctx, error):
    # 如果是 CommandInvokeError，就檢查原本引發錯誤的型別
        if isinstance(error, commands.CommandInvokeError):
            if isinstance(error.original, ValueError):
            # 如果是 ValueError，就提醒使用者輸入整數
                await ctx.send("請輸入一個整數.w.")
        else:
            # 如果不是 ValueError，就提醒使用者尚未開始遊戲
            await ctx.send(f"{ctx.author.mention} 你還沒開始遊戲！請輸入 f!guess 開始遊戲")

async def setup(bot):
    await bot.add_cog(Game(bot))
