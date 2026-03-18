# Fractal Morph MCP Server

**Falconer's random fractals with biological morphology integration**

Based on Dr. İrem Hafız's "A New Aesthetics of Vastness: Complex Fractal Geometries in Generative AI" (GA2024) and Kenneth Falconer's *Fractal Geometry: Mathematical Foundations and Applications*.

## Overview

This MCP server implements Falconer's framework for creating "random fractals" — irregular, non-uniform fractal patterns that closely resemble natural structures. Unlike regular fractals (perfectly symmetrical, predictable), random fractals introduce controlled variations that create natural-looking complexity.

### Key Innovation

**Cross-domain biological → fractal transformation**: Maps structural properties from biological systems (anthrobots, cells, organisms) to mathematical fractal parameters, enabling visualization of biological morphology as abstract geometric art.

## Three-Layer Lushy Architecture

```
Layer 1: Pure Taxonomy (0 tokens)
├── Base fractal types (Koch, Sierpinski, Hilbert, etc.)
├── Falconer's five modifications
├── Complexity vocabulary
└── Color palettes & rendering styles

Layer 2: Deterministic Mapping (0 tokens)
├── Biological → fractal parameter transformation
├── Complexity computation from parameters
└── Visual vocabulary assembly

Layer 3: Synthesis Preparation (~100-200 tokens)
└── Complete parameter set for Claude to synthesize
```

**Cost savings**: 60-98% vs iterative LLM generation (Dr. Hafız's DALL-E approach)

## Falconer's Five Modifications

From Hafız (GA2024): These transformations convert regular fractals into natural-looking forms:

1. **Irregular Recursion**: Unequal subdivision (breaks symmetry)
2. **Angle Variance**: Varying branch angles (organic branching)
3. **Iteration Depth Variation**: Spatial detail contrast (texture complexity)
4. **Curve Introduction**: Straight → curved segments (biomorphic softening)
5. **Dimension Manipulation**: Adjust space-filling character (1.0 - 3.0)

## Usage Examples

### Direct Fractal Generation

```python
# Generate Koch snowflake with high natural variation
result = fractal-morph-mcp.generate_fractal_parameters(
    base_type="koch_snowflake",
    recursion_irregularity=0.75,    # High irregularity
    angle_variance=0.45,             # Moderate angle variation
    iteration_depth_variation=0.85,  # High detail contrast
    curve_introduction=0.60,         # Organic curves
    color_palette="biological",
    rendering_style="gradient_shading"
)

# Claude synthesizes from result['visual_vocabulary']
```

### Biological → Fractal Transformation

```python
# Map anthrobot morphology to fractal
result = fractal-morph-mcp.generate_from_anthrobot(
    morphotype="football",           # Elongated form
    symmetry="bilateral",            # Bilateral symmetry
    movement_type="straight_line",   # Directional motion
    cilia_density="dense",           # Rich surface detail
    life_stage="peak_maturity",      # Full complexity
    color_palette="biological",
    rendering_style="filled_regions"
)

# Returns:
# - base_fractal_type: "hilbert_curve" (elongated → space-filling)
# - recursion_irregularity: 0.45 (bilateral → moderate)
# - angle_variance: 0.10 (straight_line → low variance)
# - iteration_depth_variation: 0.90 (dense cilia → high detail)
# - curve_introduction: 0.65 (peak_maturity → organic)
# - biological_origin: full provenance tracking
```

### Complexity Analysis

```python
# Compute complexity metrics from parameters
complexity = fractal-morph-mcp.compute_fractal_complexity(
    recursion_irregularity=0.75,
    angle_variance=0.45,
    iteration_depth_variation=0.85,
    curve_introduction=0.60,
    fractal_dimension=2.1
)

# Returns:
# - complexity_score: 0.683
# - complexity_level: "high"
# - visual_vocabulary: detailed aesthetic descriptions
# - parameter_contributions: weighted impacts
```

## Biological Mapping Framework

### Anthrobot → Fractal Correspondences

| Anthrobot Property | Maps To | Rationale |
|-------------------|---------|-----------|
| Morphotype (spheroid, sumo, football) | Base fractal type | Structural homology |
| Symmetry (radial, bilateral, asymmetric) | Recursion irregularity | Pattern correspondence |
| Movement (straight, circular, random) | Angle variance | Trajectory mapping |
| Cilia density (sparse, moderate, dense) | Iteration depth | Surface complexity |
| Life stage (progenitor → senescence) | Curve introduction | Biological maturity |

### Example: Football Anthrobot

```
Input: Football anthrobot (elongated, bilateral, straight-moving, dense cilia, mature)
    ↓
Mapping: Hilbert curve + moderate irregularity + low angle variance + high depth + organic curves
    ↓
Output: Maze-like space-filling pattern with directional bias and rich surface articulation
```

## Available Tools

### Layer 1 - Taxonomy (0 tokens)

- `list_fractal_types()` - All base fractal geometries
- `get_falconer_modifications()` - Five modification types
- `get_complexity_vocabulary()` - Visual descriptors
- `get_intentionality_principles()` - Aesthetic framework

### Layer 2 - Mapping (0 tokens)

- `map_anthrobot_to_fractal()` - Biological → fractal parameters
- `compute_fractal_complexity()` - Aggregate complexity metrics

### Layer 3 - Generation (~100-200 tokens)

- `generate_fractal_parameters()` - Direct fractal specification
- `generate_from_anthrobot()` - Complete biological pipeline

### Utilities

- `suggest_composition_domains()` - Cross-domain opportunities
- `get_research_attribution()` - Citations and sources

## Color Palettes

- **monochrome**: Pure mathematical clarity (black on white)
- **thermal**: Heat map (blue → red by recursion depth)
- **biological**: Fluorescence microscopy (cyan/magenta/yellow)
- **cosmic**: Deep space nebula (purple/blue/orange/gold)

## Rendering Styles

- **line_art**: Single continuous line, vector-style
- **filled_regions**: Solid shapes, stained-glass effect
- **gradient_shading**: Volumetric depth, sculptural
- **particle_trace**: Stippling, point cloud, atmospheric

## Theoretical Framework

### Hafız's "Aesthetics of Vastness"

> "Data-driven artistry in AI produces 'non-standard' fractal models emerging out of vast quantities of data, rather than static, symmetrical, and predictable fractal patterns."

**Computational vastness** (parameter space size) → **Formal complexity** (non-standard forms) → **Perceptual unboundedness** (sublime aesthetic experience)

### Kant's Sublime

The extreme complexity fractals overwhelm imagination's ability to "bound" or comprehend the object, triggering sublime aesthetic response: awe, astonishment, wonder.

### Falconer's Natural Resemblance

> "The randomness in these constructions leads to irregular, non-uniform curves that closely resemble the geometries seen in Nature."

Random fractals bridge mathematics and biology through shared structural principles.

## Cost Optimization

### Dr. Hafız's Iterative DALL-E Approach

```
Iteration 1: Generate base fractal ($0.04)
Iteration 2: "Make it more complex" ($0.04)
Iteration 3: "Increase variation" ($0.04)
Iteration 4: "Add irregularity" ($0.04)
Total: $0.16+ per fractal
```

### This Server's Categorical Approach

```
Layer 1: Taxonomy lookup (0 tokens, $0)
Layer 2: Deterministic mapping (0 tokens, $0)
Layer 3: Single synthesis (~150 tokens, ~$0.003)
Total: $0.003 per fractal
```

**Savings**: 98% cost reduction, deterministic repeatability, full provenance tracking.

## Composition Opportunities

### Compatible Lushy Domains

- **anthrobot-morphology-mcp**: Direct integration (implemented)
- **catastrophe-morph-mcp**: Shared geometric sharpness/bifurcation structure
- **diatom-morph-mcp**: Radial symmetry, surface perforation patterns
- **chimeric-sorting-mcp**: Emergent complexity, attractor dynamics

### Example Cross-Domain Workflow

```python
# 1. Get anthrobot parameters
anthrobot = anthrobot-morphology-mcp.generate_anthrobot_parameters(
    morphotype="spheroid",
    life_stage="peak_maturity"
)

# 2. Transform to fractal
fractal = fractal-morph-mcp.generate_from_anthrobot(
    **anthrobot.extract_morphology()
)

# 3. Apply catastrophe aesthetic
enhanced = catastrophe-morph-mcp.enhance_with_catastrophe(
    base_params=fractal,
    catastrophe_type="cusp",
    emphasis="edges"
)

# 4. Claude synthesizes final image
```

## Research Attribution

**Primary Mathematical Foundation:**
- Falconer, Kenneth. *Fractal Geometry: Mathematical Foundations and Applications.* Chichester: John Wiley & Sons, 2003.

**Aesthetic Framework:**
- Hafız, İrem. "A New Aesthetics of Vastness: Complex Fractal Geometries in Generative AI." XXVII Generative Art Conference - GA2024, 2024.
- Hafız, İrem. "Towards an Aesthetic Discourse of Computational Design: Re-contextualizing the Sublime." PhD dissertation, Middle East Technical University, 2024.

**Non-Standard Forms:**
- Mennan, Zeynep. "The Question of Non-Standard Form." *METU Journal of the Faculty of Architecture*, 25(2), 2008.

**Biological Integration:**
- Levin, Michael. Morphological computation framework. Allen Discovery Center, Tufts University.

## Installation

```bash
# Clone or download server
cd fractal-morph-mcp

# Install dependencies
pip install -e .

# Run locally
python server.py

# Or deploy to FastMCP Cloud
fastmcp deploy server.py:mcp
```

## Technical Details

- **Python**: 3.10+
- **Framework**: FastMCP
- **Dependencies**: pyyaml
- **Cost**: ~$0.003 per generation
- **Latency**: <100ms for Layer 1+2, variable for Layer 3 (Claude synthesis)

## License

Research implementation following open academic principles. Cite Hafız (2024) and Falconer (2003) in derivative work.

---

**Built by**: Dal Marsters (Lushy)  
**Contact**: dal@lushy.ai  
**Framework**: Three-layer categorical composition architecture  
**Version**: 1.0.0
