import sys


def get_new_version():
    version = sys.argv[2]
    version_update_type = sys.argv[3]
    version_update_type = version_update_type.title()
    version_breakdown = str(version)
    version_breakdown = version_breakdown.split(".")
    new_version = version
    if version_update_type == "Major":
        new_version = int(version_breakdown[0]) + 1
        new_version = f"{new_version}.0.0"
    elif version_update_type == "Minor":
        new_version = int(version_breakdown[1]) + 1
        new_version = f"{version_breakdown[0]}.{new_version}.0"
    elif version_update_type == "Patch":
        new_version = int(version_breakdown[2]) + 1
        new_version = f"{version_breakdown[0]}.{version_breakdown[1]}.{new_version}"
    return new_version


def get_commit_message():
    version = sys.argv[2]
    version_update_type = sys.argv[3]
    commit_message = f"Bitbucket Pipeline Automated Release: {version_update_type} Release with tag {version}"
    return commit_message


def main():
    choice = sys.argv[1]
    if choice == "version":
        return get_new_version()
    elif choice == "commit_message":
        return get_commit_message()
    else:
        return "invalid input"


if __name__ == "__main__":
    print(main())