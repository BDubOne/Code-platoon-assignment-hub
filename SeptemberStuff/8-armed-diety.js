const tools = ["lotus", "thunderBolt", "sword", "cup", "conch", "bow", "scroll", "discus"];
const startingTool = tools[1];
const toolCount = tools[2];
const days = 30;

function howMany(tools, startingTool, toolCount, days) {
let times = 0;
if (startingTool === toolCount) {
    times+= 1;
};
for (let i = tools.indexOf(startingTool); i <tools.length; i++) {
   days--;
   if (tools[i] === toolCount) {
        times++;
    };
    if (days <= 0) {
        console.log(times);
        return times;
    }
}
let recurringCount = function() {
    for (let i = 0; i< tools.length; i++) {
        days--;
        if (tools[i] === toolCount) {
                times++;
           }
    }

}
while (days > 0) {
   recurringCount()
    }


console.log(times)

}
howMany(["lotus", "thunderBolt", "sword", "cup", "conch", "bow", "scroll", "discus"],tools[0],tools[4],45)



