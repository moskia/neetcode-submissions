class LRUCache {
    private capacity: number;
    private cache: Map<number, CacheNode>;
    private head: CacheNode;
    private tail: CacheNode; 
    /**
     * @param {number} capacity
     */
    constructor(capacity: number) {
        this.capacity = capacity;
        this.cache = new Map<number, CacheNode>();

        this.head = new CacheNode(0, 0);
        this.tail = new CacheNode(0, 0);

        this.head.next = this.tail;
        this.tail.prev = this.head;

    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key: number): number {
        const node: CacheNode = this.cache.get(key);
        if (!node) return -1;

        this.removeNode(node);
        this.addToHead(node);
        return node.value;
        
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key: number, value: number): void {
        const existingNode =this.cache.get(key);

        if (existingNode) {
            existingNode.value = value;
            this.removeNode(existingNode);
            this.addToHead(existingNode);

            return;
        }

        const newNode = new CacheNode(key, value);
        this.cache.set(key, newNode);
        this.addToHead(newNode);

        if (this.cache.size > this.capacity) {
            let leastRecentlyUsed = this.tail.prev;

            if (leastRecentlyUsed && leastRecentlyUsed.prev !== this.head) {
                this.cache.delete(leastRecentlyUsed.key);
                this.removeNode(leastRecentlyUsed);
            }
        }

    }

    /**
     * @param {CacheNode} node
     * @return {void}
     */
    private removeNode(node: CacheNode): void {
        const prevNode = node.prev;
        const nextNode = node.next;

        if (prevNode) {
            prevNode.next = nextNode; 
        }

        if (nextNode) {
            nextNode.prev = prevNode;
        }
    }

    /**
     * @param {CacheNode}
     * @return {void}
     */

    private addToHead(node: CacheNode): void {
        const firstNode: CacheNode = this.head.next;
        this.head.next = node;
        node.prev = this.head;
        node.next = firstNode;

        if (firstNode) {
            firstNode.prev = node;
        }
    }
}

class CacheNode {
    key: number;
    value: number;
    prev: CacheNode | null=null;
    next: CacheNode | null=null;

    constructor(key: number, value: number) {
        this.key = key;
        this.value = value;
    }
}