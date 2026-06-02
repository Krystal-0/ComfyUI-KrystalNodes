import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "Krystal.MultiImagePreview",
    async nodeCreated(node) {
        if (node.comfyClass !== "MultiImagePreview") return;

        function addEmptySlot() {
            const index = node.inputs ? node.inputs.length + 1 : 1;
            node.addInput(`image_${index}`, "IMAGE");
        }

        node.onConnectionsChange = function(type, index, connected, link_info) {
            if (type !== 1) return;

            while (node.inputs.length > 1 && node.inputs[node.inputs.length - 1].link === null) {
                node.removeInput(node.inputs.length - 1);
            }

            if (node.inputs[node.inputs.length - 1].link !== null) {
                addEmptySlot();
            }
        }

        if (!node.inputs || node.inputs.length === 0) {
            addEmptySlot();
        }
    }
});