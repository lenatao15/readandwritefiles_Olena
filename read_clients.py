def main():
    try:
        with open('clients.txt', 'r') as infile:
            with open('numbered_clients.txt', 'w') as outfile:
                counter = 1
                for line in infile:
                    client_name = line.rstrip('\n')
                    outfile.write(f'{counter}. {client_name}\n')
                    counter += 1
        
        print("Successfully created 'numbered_clients.txt'")
    except FileNotFoundError:
        print("Error: 'clients.txt' not found.")

if __name__ == "__main__":
    main()