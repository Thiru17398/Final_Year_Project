const mongoose = require("mongoose");

const JourneySchema = new mongoose.Schema({
    startingPoint: {
        type: String,
        required: [true, "Starting point is required"],
    },
    endingPoint: {
        type: String,
        required: [true, "Ending point is required"],
    },
    duration: {
        type: String,
        required: [true, "Duration is required"],
    },
    cost: {
        type: String,
        required: [true, "Cost is required"],
    },
    frequency: {
        type: String,
        required: [true, "Frequency is required"],
    },
    experience: {
        type: String,
        required: [true, "Experience details are required"],
    }
});

const JourneyDetailsSchema = new mongoose.Schema({
    source: {
        type: String,
        required: [true, "Source location is required"],
    },
    destination: {
        type: String,
        required: [true, "Destination location is required"],
    },
    journeys: {
        type: [JourneySchema], // Embedding multiple journey objects
        required: true,
        validate: [(val) => val.length > 0, "At least one journey must be provided"],
    }
}, { timestamps: true });

const JourneyDetails = mongoose.model("JourneyDetails", JourneyDetailsSchema);
module.exports = JourneyDetails;
