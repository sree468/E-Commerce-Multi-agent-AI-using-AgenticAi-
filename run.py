from app.database.seed import seed_database


def main():

    print()
    print("==============================================")
    print(" E-COMMERCE MULTI-AGENT AI SYSTEM")
    print("==============================================")
    print()

    # Initialize database
    seed_database()

    print()
    print("Database setup completed.")
    print()
    print("To start the Streamlit application, run:")
    print()
    print("streamlit run ui/streamlit_app.py")
    print()


if __name__ == "__main__":
    main()