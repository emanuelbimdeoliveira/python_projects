from app import App
from controller import controller

def main():
    app = App(handle_execute=controller)
    app.mainloop()

if __name__ == "__main__":
    main()