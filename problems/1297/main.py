D,H,W=map(int, input().split())
print(int(((D**2/(H**2+W**2))*H**2)**0.5),int(((D**2/(H**2+W**2))*W**2)**0.5))