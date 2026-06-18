class LogSystem:

    def __init__(self):
        self.logs = []


    def put(self,id,timestamp):
        self.logs.append((id,timestamp))  # Store a new log entry as a (id, timestamp) tuple in self.logs


    def retrieve(self, start, end , granularity):
        granularity_map = {
            
            "Year": 4,  # THE COUNT IS THE NUMBER OF CHARACTERS TO TRUNCATE
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }
        length = granularity_map[granularity]
        start_truncated = start[:length] #length goes back to the granularity_map[granularity]
        end_truncated = end[:length]

        result = [] # store results in tthis list 
        for id, timestamp in self.logs: # Loop through all stored logs and filter by time range
                log_truncated =  timestamp[:length]
                if start_truncated <= log_truncated <= end_truncated:
                    result.append(id)


        return result
            

# Create a new log system instance
logSystem = LogSystem()

# Add three sample logs with different timestamps
logSystem = LogSystem()
logSystem.put(1, "2017:01:01:23:59:59")   
logSystem.put(2, "2017:01:01:22:59:59")
logSystem.put(3, "2016:01:01:00:00:00")
# Retrieve logs within a time range at Year granularity
print(logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"))

