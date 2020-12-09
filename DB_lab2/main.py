import dataset_beckend
import movie_controller
import studio_controller
import actor_controller

if __name__ == '__main__':

    movie_controller = movie_controller.MovieController()
    studio_controller = studio_controller.StudioController()
    actor_controller = actor_controller.ActorController()
    key = 1
    while key != 0:
        print("1. Movies")
        print("2. Studios")
        print("3. Actors")
        print("4. Search")
        print("0. Quit")
        try:
            key = int(input())
        except ValueError:
            print("Incorrect input")
            key = 5

        if key == 1:
            print("1. Get all\n2. Get by name \n3.Update \n4.Create \n5.Delete "
                  "\n6.Add actor to cast \n7. Remove actor from cast")
            try:
                op = int(input())
                if op == 1:
                    movie_controller.show_movies()
                elif op == 2:
                    movie_controller.show_movie()
                elif op == 3:
                    movie_controller.update_movie()
                elif op == 4:
                    movie_controller.create_movie()
                elif op == 5:
                    movie_controller.delete_movie()
                # elif op == 6:
                #     controller.add_movie_to_movie()
                # elif op == 7:
                #     controller.delete_movie_from_movie()

            except ValueError:
                print("Incorrect input")

        elif key == 2:
            print("1. Get all\n2. Get by name \n3. Update \n4. Create \n5. Delete "
                  "\n6. Add movie to studio \n7. Remove movie from studio")
            try:
                op = int(input())
                if op == 1:
                    studio_controller.show_studios()
                elif op == 2:
                    studio_controller.show_studio()
                elif op == 3:
                    studio_controller.update_studio()
                elif op == 4:
                    studio_controller.create_studio()
                elif op == 5:
                    studio_controller.delete_studio()
                elif op == 6:
                    studio_controller.add_movie_to_studio()
                elif op == 7:
                    studio_controller.delete_movie_from_studio()

            except ValueError:
                print("Incorrect input")

        elif key == 3:
            print("1. Get all\n2. Get by name \n3. Update \n4. Create \n5. Delete "
                  "\n6. Add contract to actor \n7. Remove contract from actor \n8. Generate random actors")
            try:
                op = int(input())
                if op == 1:
                    actor_controller.show_actors()
                elif op == 2:
                    actor_controller.show_actor()
                elif op == 3:
                    actor_controller.update_actor()
                elif op == 4:
                    actor_controller.create_actor()
                elif op == 5:
                    actor_controller.delete_actor()
                elif op == 6:
                    actor_controller.add_contract_to_actor()
                elif op == 7:
                    actor_controller.delete_contract_from_actor()
                elif op == 8:
                    actor_controller.generate_random_actors()

            except ValueError:
                print("Incorrect input")
        elif key == 4:
            print("Input search word")
            search_word = input()
            res = dataset_beckend.search(search_word)
            print(f"Time: {res['time']}")
            for row in res["results"]:
                print(row)




