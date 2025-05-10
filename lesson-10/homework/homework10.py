# # TASK 1

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue: {self.due_date}\nStatus: {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added!")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"Task '{title}' marked as complete!")
                return
        print(f"Task '{title}' not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for task in self.tasks:
            print(task)
            print("-----")

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status == "Incomplete"]
        if not incomplete:
            print("No incomplete tasks.")
        for task in incomplete:
            print(task)
            print("-----")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add a Task")
        print("2. Mark a Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            new_task = Task(title, description, due_date)
            todo_list.add_task(new_task)

        elif choice == "2":
            title = input("Enter the title of the task to mark complete: ")
            todo_list.mark_task_complete(title)

        elif choice == "3":
            print("\n--- All Tasks ---")
            todo_list.list_all_tasks()

        elif choice == "4":
            print("\n--- Incomplete Tasks ---")
            todo_list.list_incomplete_tasks()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()



# TASK 2

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"""
        Title: {self.title}
        Content: {self.content}
        Author: {self.author}
        """
    
class Blog:
    def __init__(self):
        self.posts = []
    def add_post(self, post):
        self.posts.append(post)
        print(f"Post '{post.title}' added successfully!")
    
    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
        for post in self.posts:
            print(post)
    def list_posts_by_author(self, author):
        author_posts = [post for post in self.posts if post.author == author]
        if not author_posts:
            print(f"No posts found by {author}.")
        for post in author_posts:
            print(post)

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print(f" Post {title} deleted!")
                return 
            print(f" Post {title} not found!")

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                print(f"Post {title} updated!")
                return
            print(f"Post {title} not found.")

    def get_latest_posts(self, count = 3):
        latest = self.posts[-count:]
        if not latest:
            print("No posts avialable.")
        for post in latest:
            print(post)        



def main():
    blog=Blog()

    while True:
        print("\n--- Blog Menu ---")
        print("1. Add a Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            new_post = Post(title, content, author)
            blog.add_post(new_post)

        elif choice == "2":
            print("\n--- All Posts ---")
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            print(f"\n--- Posts by {author} ---")
            blog.list_posts_by_author(author)

        elif choice == "4":
            title = input("Enter post title to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Enter post title to edit: ")
            new_content = input("Enter new content: ")
            blog.edit_post(title, new_content)

        elif choice == "6":
            count = input("How many latest posts to show? (Press Enter for 3): ")
            count = int(count) if count else 3
            print(f"\n--- Latest {count} Posts ---")
            blog.get_latest_posts(count)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


# Task 3
class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account: {self.account_number}\nHolder: {self.account_holder}\nBalance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account):
        if account.account_number not in self.accounts:
            self.accounts[account.account_number] = account
            return True
        return False
    
    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    def transfer(self, from_acc_num, to_acc_num, amount):
        from_account = self.get_account(from_acc_num)
        to_account = self.get_account(to_acc_num)
        
        if not from_account or not to_account:
            return False
        
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False
    
    def display_all_accounts(self):
        for account in self.accounts.values():
            print(account)
            print("-----")

def main():
    bank = Bank()
    
    while True:
        print("\n--- Banking System Menu ---")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. View All Accounts")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            initial_deposit = float(input("Enter initial deposit: $"))
            new_account = Account(acc_num, name, initial_deposit)
            if bank.add_account(new_account):
                print("Account created successfully!")
            else:
                print("Account number already exists!")
        
        elif choice == "2":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                print(f"Balance: ${account.get_balance():.2f}")
            else:
                print("Account not found!")
        
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: $"))
            account = bank.get_account(acc_num)
            if account and account.deposit(amount):
                print("Deposit successful!")
            else:
                print("Deposit failed. Check account number/amount.")
        
        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: $"))
            account = bank.get_account(acc_num)
            if account and account.withdraw(amount):
                print("Withdrawal successful!")
            else:
                print("Withdrawal failed. Check balance/account.")
        
        elif choice == "5":
            from_acc = input("Enter your account number: ")
            to_acc = input("Enter recipient account number: ")
            amount = float(input("Enter transfer amount: $"))
            if bank.transfer(from_acc, to_acc, amount):
                print("Transfer successful!")
            else:
                print("Transfer failed. Check account numbers/balance.")
        
        elif choice == "6":
            print("\n--- All Accounts ---")
            bank.display_all_accounts()
        
        elif choice == "7":
            print("Thank you for banking with us!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()