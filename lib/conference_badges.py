def badge_maker(name):
    """Generate a badge for a given name."""
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    """Create a list of badges for a list of names."""
    badges = [badge_maker(name) for name in names]
    return badges

def assign_rooms(names):
    """Assign rooms to attendees and generate room assignments."""
    room_assignments = [f"Hello, {name}! You'll be assigned to room {i + 1}!" for i, name in enumerate(names)]
    return room_assignments

def print_badges_and_assignments(names):
    """Print badges and room assignments for all attendees."""
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)

    room_assignments = assign_rooms(names)
    for room_assignment in room_assignments:
        print(room_assignment)

if __name__ == "__main__":
    # Updated list of attendees:
    attendees = ["Stephan", "Mark", "Keren", "Bat-Tziyon", "Samuel", "Pascalia"]
    print_badges_and_assignments(attendees)
