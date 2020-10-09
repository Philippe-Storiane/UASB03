package JavaExtractor.FeaturesEntities;

import java.nio.file.Path;
import java.util.ArrayList;
import java.util.stream.Collectors;

public class ProgramTextFeatures {
    String name;

    transient StringBuffer text = new StringBuffer();

    String filePath;

    public ProgramTextFeatures(String name, Path filePath) {

        this.name = name;
        this.filePath = filePath.toAbsolutePath().toString();
    }

    @SuppressWarnings("StringBufferReplaceableByString")
    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();
	int baseLineIndex = this.filePath.lastIndexOf('/') + 1;
	String className = this.filePath.substring( baseLineIndex, this.filePath.length() - 5);
	stringBuilder.append( className).append(" "); 
        stringBuilder.append(name).append(" ");
        stringBuilder.append( text );

        return stringBuilder.toString();
    }

    public void addFeature(Property property) {
        text.append(" " ).append( property.getName());
    }

    public boolean isEmpty() {
        return this.toString().isEmpty();
    }
}
