from mastodon import Mastodon

# Create actual API instance
mastodon = Mastodon(
    access_token = 'c6d72eee8edd1242f2aae49b78cbef3f23ba35f27775fdad90b9d9766ad5e73b',
    api_base_url = 'https://mastodon.social'
)

# First toot
# mastodon.toot('Tooting via python using #mastodonpy!')

# Testing API search function
query = mastodon.search("trump")

# Write query results to 'query.txt' file
query_results = open('query.txt', 'w')
for id in query.statuses.id:
    query_results.write(id + "\n")
query_results.close()

i = 0
for status in query['statuses']:
    print(status)
    print(i)
    i += 1