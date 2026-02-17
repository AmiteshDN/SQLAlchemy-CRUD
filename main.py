import argparse
from db import init_db, SessionLocal
import crud


def cmd_demo():
    init_db()
    with SessionLocal() as s:
        print("Creating users...")
        try:
            u1 = crud.create_user(s, "alice", "alice@example.com", "Alice A")
            u2 = crud.create_user(s, "bob", "bob@example.com", "Bob B")
        except Exception as e:
            print("Create error (maybe already exist):", e)

        print("List users:")
        for u in crud.list_users(s):
            print(u)

        print("Update user 1 full_name -> 'Alice Updated'")
        updated = crud.update_user(s, 1, full_name="Alice Updated")
        print("Updated:", updated)

        print("Get user 1:", crud.get_user(s, 1))

        print("Delete user 2")
        deleted = crud.delete_user(s, 2)
        print("Deleted?", deleted)

        print("Final users:")
        for u in crud.list_users(s):
            print(u)


def main():
    parser = argparse.ArgumentParser(description="Simple SQLAlchemy CRUD demo")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("demo", help="Run demo sequence")

    p_create = sub.add_parser("create", help="Create a user")
    p_create.add_argument("username")
    p_create.add_argument("email")
    p_create.add_argument("full_name", nargs="?", default=None)

    p_get = sub.add_parser("get", help="Get user by id")
    p_get.add_argument("id", type=int)

    sub.add_parser("list", help="List users")

    p_update = sub.add_parser("update", help="Update user by id")
    p_update.add_argument("id", type=int)
    p_update.add_argument("field")
    p_update.add_argument("value")

    p_delete = sub.add_parser("delete", help="Delete user by id")
    p_delete.add_argument("id", type=int)

    args = parser.parse_args()

    init_db()

    if args.cmd == "demo" or args.cmd is None:
        cmd_demo()
        return

    with SessionLocal() as s:
        if args.cmd == "create":
            u = crud.create_user(s, args.username, args.email, args.full_name)
            print("Created:", u)
        elif args.cmd == "get":
            print(crud.get_user(s, args.id))
        elif args.cmd == "list":
            for u in crud.list_users(s):
                print(u)
        elif args.cmd == "update":
            res = crud.update_user(s, args.id, **{args.field: args.value})
            print("Updated:", res)
        elif args.cmd == "delete":
            ok = crud.delete_user(s, args.id)
            print("Deleted?", ok)


if __name__ == "__main__":
    main()
