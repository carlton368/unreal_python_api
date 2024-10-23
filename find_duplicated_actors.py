import unreal

# EditorActorSubsystem = unreal.EditorActorSubsystem()  # Unreal older than 5.3
EditorActorSubsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)  # Unreal 5.3 and newer

actors = EditorActorSubsystem.get_all_level_actors()

# Grouping objects based on name and class
actors_per_asset_groups = []
for actor in actors:
    if not isinstance(actor, unreal.StaticMeshActor):
        continue

    found = False
    for group in actors_per_asset_groups:
        if actor.static_mesh_component.static_mesh.get_full_name() == \
                group[0].static_mesh_component.static_mesh.get_full_name():
            group.append(actor)
            found = True
            break
    if not found:
        actors_per_asset_groups.append([actor])

actors_per_asset_groups = [a for a in actors_per_asset_groups if len(a) >= 2]  # clean small arrays

# Finding duplicates
duplicates_groups = []
for actors_group in actors_per_asset_groups:
    matched_indexes = []  # Indexes in the group that were iterated over already and thus will be ignored neext time

    # Iterate backwards to avoid issues caused by pop()
    for i in range(len(actors_group) - 1, -1, -1):
        if i in matched_indexes:
            continue

        current = actors_group[i]
        nearby_actors = [current]
        actors_group.pop(i)

        for j in range(len(actors_group) - 1, -1, -1):
            if j in matched_indexes:
                continue
            comparing_to = actors_group[j]
            if current.get_actor_transform().is_near_equal(comparing_to.get_actor_transform()):
                nearby_actors.append(comparing_to)
                matched_indexes.append(j)

        if len(nearby_actors) > 1:
            duplicates_groups.append(nearby_actors)

# Print result
for actors_group in duplicates_groups:
    for actor in actors_group:
        print(f"{actor.get_full_name()}  |  {actor.static_mesh_component.static_mesh.get_full_name()}  |  "
              f"{actor.get_actor_transform().translation}")
    print(20 * "-")
