
def try_import_package()-> None:
    try:
        import pandas
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ImportError:
        print("Missing pandas dependence")
        print("Install by pip : pip install pandas")
        print("Install by poetry : poetry add pandas\n")

    try:
        import requests
        print(f"[OK] requests ({requests.__version__}) - Network access ready")
    except ImportError:
        print("Missing requests dependence")
        print("Install by pip : pip install requests")
        print("Install by poetry : poetry add requests\n")

    try:
        import matplotlib
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
    except ImportError:
        print("Missing matplotlib dependence")
        print("Install by pip : pip install matplotlib")
        print("Install by poetry : poetry add matplotlib\n")

    try:
        import numpy
        print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")
    except ImportError:
        print("Missing numpy dependence")
        print("Install by pip : pip install numpy")
        print("Install by poetry : poetry add numpy\n")

def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    try_import_package()

if __name__ == "__main__":
    main()