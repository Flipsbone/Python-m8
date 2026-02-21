import sys
import os
import site


def define_env() -> dict:

    if sys.base_prefix == sys.prefix:
        status: str = "You're still plugged in"
        exec_python: str = f"{sys.executable}"
        env: str = None
        display_message: str = (
            "WARNING: You're in the global environment!\n"
            "The machines can see everything you install.\n\n"
            "To enter the construct, run:\n"
            "python -m venv matrix_env\n"
        )

        if os.name == "posix":
            display_message += "source matrix_env/bin/activate\n"

        elif os.name == "nt":
            display_message += "matrix_env\\Scripts\\activate\n"

        else:
            display_message += ("OS not recognized. Activate venv manually.\n")
        display_message += "\nThen run this program again."
        path_package: str = None

    else:
        status: str = "Welcome to the construct"
        exec_python: str = f"{sys.executable}"
        env: str = f"{sys.prefix}"
        display_message: str = (
            "SUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system.\n"
        )
        path_package: list[str] = site.getsitepackages()

    return {
        "status": status,
        "exec_python": exec_python,
        "env": env,
        "message": display_message,
        "path_package": path_package
    }


def main() -> None:
    display_result: dict = define_env()
    print(f"MATRIX STATUS: {display_result['status']}\n")
    print(f"Current Python: {display_result['exec_python']}")

    if display_result['env'] is None:
        print("Virtual Environment: None detected\n")
        print(display_result['message'])

    else:
        env_path: str = display_result['env']
        env_name: str = os.path.basename(env_path)

        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}\n")
        print(display_result['message'])

        package_path = display_result['path_package'][0]
        print("Package installation path:")
        print(package_path)


if __name__ == "__main__":
    main()
