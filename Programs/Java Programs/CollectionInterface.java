// Write a progam to demonstrate method of list interface, set of interface of map.

import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;
import java.util.List;
import java.util.Set;
import java.util.Map;

public class CollectionInterface {

    public static void main(String[] args) {
        // Demonstrating List interface
        List<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Cherry");
        list.add("Apple"); // List allows duplicate elements

        System.out.println("List elements:");
        for (String element : list) {
            System.out.println(element);
        }

        list.remove("Banana");
        System.out.println("\nList after removing 'Banana':");
        for (String element : list) {
            System.out.println(element);
        }

        // Demonstrating Set interface
        Set<String> set = new HashSet<>();
        set.add("Apple");
        set.add("Banana");
        set.add("Cherry");
        set.add("Apple"); // Set does not allow duplicate elements

        System.out.println("\nSet elements:");
        for (String element : set) {
            System.out.println(element);
        }

        set.remove("Banana");
        System.out.println("\nSet after removing 'Banana':");
        for (String element : set) {
            System.out.println(element);
        }

        // Demonstrating Map interface
        Map<String, Integer> map = new HashMap<>();
        map.put("Apple", 1);
        map.put("Banana", 2);
        map.put("Cherry", 3);
        map.put("Apple", 4); // Map allows duplicate keys, but the value will be updated

        System.out.println("\nMap elements:");
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        map.remove("Banana");
        System.out.println("\nMap after removing 'Banana':");
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}