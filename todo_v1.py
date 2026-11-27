# 1.初始化一个空列表，用于存放所有待办事项
todos = []

def show_menus():
  print("1.添加待办")
  print("2.查看全部")
  print("3.标记完成")
  print("4.退出")

# 2.主循环
while True:
  show_menus()
  choice = input("请输入你的选择")
  # 3.条件判断
  if choice == "1":
    text = input("请输入待办事项")
    new_id = len(todos) + 1
    new_todo = {
      "id": new_id,
      "text": text,
      "done": False
    }
    todos.append(new_todo)
    print(f"✅待办事项 {text} 已添加")
  elif choice == "2":
    if len(todos) == 0:
      print("🔍 没有待办事项")
    else:
      print("\n你的待办列表:")
      for item in todos:
        status = "✅" if item["done"] else "[]"
        print(f"{status} {item["id"]}. {item["text"]}")
  elif choice == "3":
    target_id_str = input("请输入要标记完成的待办ID:")
    target_id = int(target_id_str)
    fount = False
    for item in todos:
      if item["id"] == target_id:
        item["done"] = True
        print(f"✅ 待办事项 {item["text"]} 已标记完成")
        fount = True
        break
    if not fount:
      print(f"❌ 未找到ID为 {target_id} 的待办事项")
  elif choice == "4":
    print("👋 再见！")
    break
  else:
    print("❌ 无效的选择，请重新输入")
