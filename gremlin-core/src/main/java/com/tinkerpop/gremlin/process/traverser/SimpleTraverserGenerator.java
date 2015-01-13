package com.tinkerpop.gremlin.process.traverser;

import com.tinkerpop.gremlin.process.Step;
import com.tinkerpop.gremlin.process.Traverser;
import com.tinkerpop.gremlin.process.TraverserGenerator;

/**
 * @author Marko A. Rodriguez (http://markorodriguez.com)
 */
public class SimpleTraverserGenerator implements TraverserGenerator {

    private static final SimpleTraverserGenerator INSTANCE = new SimpleTraverserGenerator();

    private SimpleTraverserGenerator() {
    }

    public <S> Traverser.Admin<S> generate(final S start, final Step<S, ?> startStep, final long initialBulk) {
        final SimpleTraverser<S> traverser = new SimpleTraverser<>(start, startStep);
        traverser.setBulk(initialBulk);
        return traverser;
    }

    public static SimpleTraverserGenerator instance() {
        return INSTANCE;
    }
}
