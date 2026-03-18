#!/usr/bin/env python3
"""
Fractal Morph MCP Server
========================

Visual vocabulary for Falconer's random fractals with biological morphology integration.

Based on:
- Kenneth Falconer's "Fractal Geometry: Mathematical Foundations and Applications"
- Dr. İrem Hafız's "A New Aesthetics of Vastness" (GA2024)
- Integration with Lushy anthrobot-morphology-mcp

Three-layer Lushy architecture:
- Layer 1: Categorical fractal taxonomy (YAML olog)
- Layer 2: Deterministic biological → fractal mapping
- Layer 3: Visual parameter generation for synthesis
"""

from fastmcp import FastMCP
from typing import Dict, List, Optional, Any, Literal
from pathlib import Path
import yaml
import json
import math

# Initialize FastMCP server
mcp = FastMCP("fractal-morph")

# Load olog taxonomy
_olog_path = Path(__file__).parent / "fractal_morph.olog.yaml"
with open(_olog_path) as f:
    OLOG = yaml.safe_load(f)


# ==============================================================================
# LAYER 1 - Pure Taxonomy Retrieval (Zero LLM Cost)
# ==============================================================================

@mcp.tool()
def list_fractal_types() -> str:
    """
    List all base fractal types with their mathematical properties.
    
    Returns formatted overview of fractal taxonomy from Falconer.
    """
    fractals = OLOG['fractal_types']
    
    result = "# Base Fractal Types (Falconer Framework)\n\n"
    
    for key, data in fractals.items():
        result += f"## {data['name']}\n"
        result += f"**Type ID:** {key}\n"
        result += f"**Description:** {data['description']}\n"
        result += f"**Base Dimension:** {data['base_dimension']}\n"
        result += f"**Symmetry:** {data['symmetry']}\n"
        result += f"**Recursion Depth:** {data['typical_recursion_depth']}\n"
        result += f"**Visual Signature:** {data['visual_signature']}\n\n"
    
    return result


@mcp.tool()
def get_falconer_modifications() -> str:
    """
    Get complete taxonomy of Falconer's five modification types.
    
    These are the discrete operations that transform regular fractals 
    into "non-standard" random fractals resembling natural forms.
    
    Returns modification types with mathematical definitions and visual effects.
    """
    mods = OLOG['falconer_modifications']
    
    result = "# Falconer's Five Modifications for Random Fractals\n\n"
    result += "From Hafız (GA2024): DALL-E identified these as key transformations\n\n"
    
    for mod_type, data in mods.items():
        result += f"## {mod_type.replace('_', ' ').title()}\n"
        result += f"**Mathematical Operation:** {data['mathematical_operation']}\n"
        result += f"**Parameter Range:** {data['parameter_range']}\n"
        result += f"**Visual Effect:** {data['visual_effect']}\n"
        result += f"**Natural Analog:** {data['natural_analog']}\n\n"
    
    return result


@mcp.tool()
def get_complexity_vocabulary() -> str:
    """
    Get complete visual vocabulary for fractal complexity levels.
    
    Maps numerical parameters to aesthetic descriptions.
    """
    vocab = OLOG['complexity_vocabulary']
    
    result = "# Fractal Complexity Vocabulary\n\n"
    
    for level_key, data in vocab.items():
        result += f"## {level_key.replace('_', ' ').title()}\n"
        result += f"**Range:** {data['range']}\n"
        result += f"**Visual Character:** {data['visual_character']}\n"
        result += f"**Surface Quality:** {data['surface_quality']}\n"
        result += f"**Edge Definition:** {data['edge_definition']}\n"
        result += f"**Perceptual Impact:** {data['perceptual_impact']}\n\n"
    
    return result


@mcp.tool()
def get_intentionality_principles() -> str:
    """
    Get core intentionality explaining fractal aesthetics framework.
    
    Returns Hafız's "aesthetics of vastness" and Falconer's mathematical foundation.
    """
    intent = OLOG['intentionality']
    
    result = "# Fractal Morph Intentionality Principles\n\n"
    
    result += f"## Core Principle: {intent['core_principle']['concept']}\n"
    result += f"{intent['core_principle']['explanation']}\n\n"
    
    result += f"### Hafız Framework:\n{intent['core_principle']['hafiz_framework']}\n\n"
    
    # Individual principles
    principles = [
        ('vastness_through_variation', 'Vastness Through Variation'),
        ('natural_resemblance', 'Natural Resemblance'),
        ('sublime_unboundedness', 'Sublime Unboundedness'),
        ('data_driven_emergence', 'Data-Driven Emergence')
    ]
    
    for key, title in principles:
        data = intent[key]
        result += f"## {title}\n"
        result += f"**Principle:** {data['principle']}\n"
        result += f"**Implementation:** {data['implementation']}\n"
        result += f"**Visual Result:** {data['visual_result']}\n\n"
    
    return result


# ==============================================================================
# LAYER 2 - Deterministic Mapping (Zero LLM Cost)
# ==============================================================================

def _map_value_to_range(value: float, in_min: float, in_max: float, 
                        out_min: float, out_max: float) -> float:
    """Linear interpolation helper."""
    return out_min + (value - in_min) * (out_max - out_min) / (in_max - in_min)


def _clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp value to range."""
    return max(min_val, min(max_val, value))


def _map_anthrobot_to_fractal_impl(
    morphotype: str,
    symmetry: str,
    movement_type: str,
    cilia_density: str,
    life_stage: str
) -> Dict[str, Any]:
    """
    Core implementation of anthrobot → fractal mapping.
    
    This is a helper function that can be called by both the tool and other functions.
    """
    # Morphotype → Base fractal type
    morphotype_map = {
        "spheroid": "koch_snowflake",      # Radial symmetry
        "sumo": "sierpinski_carpet",       # Dense, space-filling
        "football": "hilbert_curve"        # Elongated, directional
    }
    base_fractal = morphotype_map[morphotype]
    
    # Symmetry → Recursion irregularity
    symmetry_map = {
        "radial": 0.15,      # Low irregularity (symmetrical)
        "bilateral": 0.45,   # Moderate irregularity
        "asymmetric": 0.85   # High irregularity (natural-looking)
    }
    recursion_irregularity = symmetry_map[symmetry]
    
    # Movement → Angle variance
    movement_map = {
        "straight_line": 0.10,   # Low variance (predictable)
        "circular": 0.35,        # Moderate variance
        "random_walk": 0.75      # High variance (chaotic)
    }
    angle_variance = movement_map[movement_type]
    
    # Cilia density → Iteration depth variation
    cilia_map = {
        "sparse": 0.25,      # Low depth variation
        "moderate": 0.55,    # Moderate depth
        "dense": 0.90        # High depth (complex surface)
    }
    iteration_depth_var = cilia_map[cilia_density]
    
    # Life stage → Curve introduction (biological forms = more curves)
    stage_map = {
        "progenitor": 0.05,      # Minimal curves (rigid)
        "early_maturity": 0.25,
        "peak_maturity": 0.65,   # Organic curves
        "late_maturity": 0.85,
        "senescence": 0.95       # Maximum organic character
    }
    curve_introduction = stage_map[life_stage]
    
    # Compute fractal dimension from overall complexity
    # Base dimension from fractal type, modified by parameters
    base_dims = {
        "koch_snowflake": 1.26,
        "sierpinski_carpet": 1.89,
        "hilbert_curve": 2.0,
        "dragon_curve": 1.52,
        "sierpinski_triangle": 1.58
    }
    base_dim = base_dims[base_fractal]
    
    # Increase dimension with complexity
    complexity_factor = (recursion_irregularity + iteration_depth_var) / 2
    fractal_dimension = base_dim + (complexity_factor * 0.4)  # Max +0.4 to dimension
    
    return {
        "base_fractal_type": base_fractal,
        "falconer_parameters": {
            "recursion_irregularity": recursion_irregularity,
            "angle_variance": angle_variance,
            "iteration_depth_variation": iteration_depth_var,
            "curve_introduction": curve_introduction,
            "fractal_dimension": round(fractal_dimension, 2)
        },
        "mapping_rationale": {
            "morphotype": f"{morphotype} → {base_fractal} (structural homology)",
            "symmetry": f"{symmetry} → irregularity {recursion_irregularity} (pattern correspondence)",
            "movement": f"{movement_type} → angle variance {angle_variance} (trajectory mapping)",
            "cilia": f"{cilia_density} → depth variation {iteration_depth_var} (surface complexity)",
            "stage": f"{life_stage} → curve intro {curve_introduction} (biological maturity)"
        },
        "biological_origin": {
            "source_system": "anthrobot",
            "morphotype": morphotype,
            "symmetry": symmetry,
            "movement": movement_type,
            "cilia_density": cilia_density,
            "life_stage": life_stage
        }
    }


@mcp.tool()
def map_anthrobot_to_fractal(
    morphotype: Literal["spheroid", "sumo", "football"],
    symmetry: Literal["radial", "bilateral", "asymmetric"],
    movement_type: Literal["straight_line", "circular", "random_walk"],
    cilia_density: Literal["sparse", "moderate", "dense"],
    life_stage: Literal["progenitor", "early_maturity", "peak_maturity", "late_maturity", "senescence"]
) -> Dict[str, Any]:
    """
    Map anthrobot morphological parameters to fractal parameters.
    
    LAYER 2 DETERMINISTIC OPERATION - 0 tokens
    
    Implements biological → fractal transformation based on structural homology:
    - Anthrobot morphotype → Base fractal type
    - Symmetry pattern → Recursion irregularity
    - Movement pattern → Angle variance
    - Cilia density → Surface complexity (iteration depth)
    - Life stage → Overall complexity level
    
    Args:
        morphotype: Anthrobot body form
        symmetry: Symmetry pattern
        movement_type: Locomotion pattern
        cilia_density: Ciliary corona density
        life_stage: Developmental stage
    
    Returns:
        Complete fractal parameter set ready for generation
    """
    return _map_anthrobot_to_fractal_impl(
        morphotype=morphotype,
        symmetry=symmetry,
        movement_type=movement_type,
        cilia_density=cilia_density,
        life_stage=life_stage
    )


def _compute_fractal_complexity_impl(
    recursion_irregularity: float,
    angle_variance: float,
    iteration_depth_variation: float,
    curve_introduction: float,
    fractal_dimension: float
) -> Dict[str, Any]:
    """
    Core implementation of complexity computation.
    
    This is a helper function that can be called by both the tool and other functions.
    """
    # Weighted complexity score
    complexity_score = (
        recursion_irregularity * 0.25 +
        angle_variance * 0.20 +
        iteration_depth_variation * 0.30 +
        curve_introduction * 0.15 +
        ((fractal_dimension - 1.0) / 2.0) * 0.10  # Normalize dimension to 0-1
    )
    
    # Classify complexity level
    if complexity_score < 0.25:
        level = "minimal"
        vocab = OLOG['complexity_vocabulary']['minimal']
    elif complexity_score < 0.50:
        level = "moderate"
        vocab = OLOG['complexity_vocabulary']['moderate']
    elif complexity_score < 0.75:
        level = "high"
        vocab = OLOG['complexity_vocabulary']['high']
    else:
        level = "extreme"
        vocab = OLOG['complexity_vocabulary']['extreme']
    
    return {
        "complexity_score": round(complexity_score, 3),
        "complexity_level": level,
        "visual_vocabulary": vocab,
        "parameter_contributions": {
            "recursion_irregularity_impact": round(recursion_irregularity * 0.25, 3),
            "angle_variance_impact": round(angle_variance * 0.20, 3),
            "iteration_depth_impact": round(iteration_depth_variation * 0.30, 3),
            "curve_introduction_impact": round(curve_introduction * 0.15, 3),
            "dimension_impact": round(((fractal_dimension - 1.0) / 2.0) * 0.10, 3)
        },
        "aesthetic_recommendation": {
            "edge_treatment": vocab['edge_definition'],
            "surface_quality": vocab['surface_quality'],
            "visual_density": vocab['visual_character']
        }
    }


@mcp.tool()
def compute_fractal_complexity(
    recursion_irregularity: float,
    angle_variance: float,
    iteration_depth_variation: float,
    curve_introduction: float,
    fractal_dimension: float
) -> Dict[str, Any]:
    """
    Compute aggregate complexity metrics from Falconer parameters.
    
    LAYER 2 DETERMINISTIC OPERATION - 0 tokens
    
    Returns complexity classification and visual vocabulary recommendations.
    
    Args:
        recursion_irregularity: 0.0-1.0
        angle_variance: 0.0-1.0
        iteration_depth_variation: 0.0-1.0
        curve_introduction: 0.0-1.0
        fractal_dimension: 1.0-3.0
    
    Returns:
        Complexity level, visual vocabulary, and aesthetic recommendations
    """
    return _compute_fractal_complexity_impl(
        recursion_irregularity,
        angle_variance,
        iteration_depth_variation,
        curve_introduction,
        fractal_dimension
    )


# ==============================================================================
# LAYER 3 - Visual Parameter Generation for Synthesis
# ==============================================================================

def _generate_fractal_parameters_impl(
    base_type: str,
    recursion_irregularity: float = 0.5,
    angle_variance: float = 0.3,
    iteration_depth_variation: float = 0.4,
    curve_introduction: float = 0.2,
    fractal_dimension: Optional[float] = None,
    color_palette: str = "monochrome",
    rendering_style: str = "line_art"
) -> Dict[str, Any]:
    """
    Core implementation of fractal parameter generation.
    
    This is a helper function that can be called by both the tool and other functions.
    """
    # Get base fractal properties
    fractal_def = OLOG['fractal_types'][base_type]
    
    # Compute or use provided dimension
    if fractal_dimension is None:
        base_dim = fractal_def['base_dimension']
        complexity = (recursion_irregularity + iteration_depth_variation) / 2
        fractal_dimension = base_dim + (complexity * 0.4)
    
    fractal_dimension = _clamp(fractal_dimension, 1.0, 3.0)
    
    # Compute complexity metrics
    complexity_data = _compute_fractal_complexity_impl(
        recursion_irregularity,
        angle_variance,
        iteration_depth_variation,
        curve_introduction,
        fractal_dimension
    )
    
    # Get color palette
    palette_def = OLOG['color_palettes'][color_palette]
    
    # Get rendering style
    render_def = OLOG['rendering_styles'][rendering_style]
    
    # Build visual vocabulary
    visual_vocab = {
        "base_geometry": {
            "fractal_name": fractal_def['name'],
            "base_symmetry": fractal_def['symmetry'],
            "fundamental_shape": fractal_def['visual_signature']
        },
        
        "modification_effects": {
            "irregularity": {
                "level": recursion_irregularity,
                "visual_effect": "uniform recursion" if recursion_irregularity < 0.3 
                                else "moderate variation" if recursion_irregularity < 0.7
                                else "chaotic natural-looking divisions",
                "edge_character": "crisp mathematical" if recursion_irregularity < 0.3
                                 else "organic irregular" if recursion_irregularity < 0.7
                                 else "rough natural boundaries"
            },
            
            "angle_variance": {
                "level": angle_variance,
                "visual_effect": "rigid geometric angles" if angle_variance < 0.3
                                else "gentle angle deviation" if angle_variance < 0.7
                                else "wildly varying angles resembling growth",
                "branching_character": "predictable" if angle_variance < 0.3
                                      else "semi-organic" if angle_variance < 0.7
                                      else "naturalistic branching"
            },
            
            "depth_variation": {
                "level": iteration_depth_variation,
                "visual_effect": "uniform detail level" if iteration_depth_variation < 0.3
                                else "variable detail regions" if iteration_depth_variation < 0.7
                                else "dramatic detail contrast",
                "surface_quality": "smooth consistent" if iteration_depth_variation < 0.3
                                  else "textured varied" if iteration_depth_variation < 0.7
                                  else "richly articulated landscape"
            },
            
            "curve_intro": {
                "level": curve_introduction,
                "visual_effect": "sharp straight segments" if curve_introduction < 0.3
                                else "gentle curves blending" if curve_introduction < 0.7
                                else "flowing organic curves dominating",
                "form_character": "crystalline rigid" if curve_introduction < 0.3
                                 else "balanced geometry-organic" if curve_introduction < 0.7
                                 else "biomorphic fluid"
            }
        },
        
        "aggregate_properties": {
            "fractal_dimension": round(fractal_dimension, 2),
            "complexity_level": complexity_data['complexity_level'],
            "visual_density": complexity_data['visual_vocabulary']['visual_character'],
            "edge_definition": complexity_data['visual_vocabulary']['edge_definition'],
            "surface_quality": complexity_data['visual_vocabulary']['surface_quality'],
            "perceptual_impact": complexity_data['visual_vocabulary']['perceptual_impact']
        },
        
        "color_specification": palette_def,
        
        "rendering_approach": render_def,
        
        "aesthetic_framework": {
            "reference": "Hafız (GA2024) - Aesthetics of Vastness",
            "principle": "Random fractals via Falconer modifications create natural resemblance",
            "sublime_quality": complexity_data['visual_vocabulary']['perceptual_impact']
        }
    }
    
    return {
        "fractal_specification": {
            "base_type": base_type,
            "dimension": round(fractal_dimension, 2),
            "complexity_score": complexity_data['complexity_score']
        },
        
        "falconer_parameters": {
            "recursion_irregularity": recursion_irregularity,
            "angle_variance": angle_variance,
            "iteration_depth_variation": iteration_depth_variation,
            "curve_introduction": curve_introduction
        },
        
        "visual_vocabulary": visual_vocab,
        
        "synthesis_guidance": f"""
        CREATE: {fractal_def['name']} with {complexity_data['complexity_level']} complexity
        
        BASE FORM: {fractal_def['visual_signature']}
        MODIFICATIONS: Apply Falconer's random variations
          - Recursion: {visual_vocab['modification_effects']['irregularity']['visual_effect']}
          - Angles: {visual_vocab['modification_effects']['angle_variance']['visual_effect']}
          - Depth: {visual_vocab['modification_effects']['depth_variation']['visual_effect']}
          - Curves: {visual_vocab['modification_effects']['curve_intro']['visual_effect']}
        
        VISUAL CHARACTER: {visual_vocab['aggregate_properties']['visual_density']}
        EDGE QUALITY: {visual_vocab['aggregate_properties']['edge_definition']}
        SURFACE: {visual_vocab['aggregate_properties']['surface_quality']}
        
        COLORS: {palette_def['description']}
        RENDERING: {render_def['description']}
        
        AESTHETIC: {visual_vocab['aggregate_properties']['perceptual_impact']}
        Evoke the sublime through data-driven vastness and natural resemblance.
        """
    }


@mcp.tool()
def generate_fractal_parameters(
    base_type: Literal["koch_snowflake", "koch_curve", "sierpinski_triangle", 
                       "sierpinski_carpet", "dragon_curve", "hilbert_curve", "peano_curve"],
    recursion_irregularity: float = 0.5,
    angle_variance: float = 0.3,
    iteration_depth_variation: float = 0.4,
    curve_introduction: float = 0.2,
    fractal_dimension: Optional[float] = None,
    color_palette: Literal["monochrome", "thermal", "biological", "cosmic"] = "monochrome",
    rendering_style: Literal["line_art", "filled_regions", "gradient_shading", "particle_trace"] = "line_art"
) -> Dict[str, Any]:
    """
    Generate complete visual parameters for fractal synthesis.
    
    LAYER 3 SYNTHESIS PREPARATION - Returns parameters for Claude to synthesize
    
    This is the main generation tool. Accepts direct Falconer parameters or 
    use map_anthrobot_to_fractal() first to convert biological structures.
    
    Args:
        base_type: Base fractal geometry
        recursion_irregularity: Deviation from uniform recursion (0.0-1.0)
        angle_variance: Deviation from base angles (0.0-1.0)
        iteration_depth_variation: Spatial variation in recursion depth (0.0-1.0)
        curve_introduction: Amount of curve vs straight segments (0.0-1.0)
        fractal_dimension: Override computed dimension (1.0-3.0)
        color_palette: Color scheme selection
        rendering_style: Visualization approach
    
    Returns:
        Complete parameter set ready for Claude synthesis
    """
    return _generate_fractal_parameters_impl(
        base_type=base_type,
        recursion_irregularity=recursion_irregularity,
        angle_variance=angle_variance,
        iteration_depth_variation=iteration_depth_variation,
        curve_introduction=curve_introduction,
        fractal_dimension=fractal_dimension,
        color_palette=color_palette,
        rendering_style=rendering_style
    )


@mcp.tool()
def generate_from_anthrobot(
    morphotype: Literal["spheroid", "sumo", "football"],
    symmetry: Literal["radial", "bilateral", "asymmetric"],
    movement_type: Literal["straight_line", "circular", "random_walk"],
    cilia_density: Literal["sparse", "moderate", "dense"],
    life_stage: Literal["progenitor", "early_maturity", "peak_maturity", "late_maturity", "senescence"],
    color_palette: Literal["monochrome", "thermal", "biological", "cosmic"] = "biological",
    rendering_style: Literal["line_art", "filled_regions", "gradient_shading", "particle_trace"] = "filled_regions"
) -> Dict[str, Any]:
    """
    Complete pipeline: Anthrobot morphology → Fractal parameters → Visual synthesis.
    
    CONVENIENCE WRAPPER combining Layer 2 mapping + Layer 3 generation
    
    This implements Dr. Hafız's complete workflow:
    1. Extract biological structure (from anthrobot-morphology-mcp)
    2. Map to fractal parameters (Layer 2 deterministic)
    3. Generate visual vocabulary (Layer 3 synthesis prep)
    
    Args:
        morphotype: Anthrobot body form
        symmetry: Symmetry pattern
        movement_type: Locomotion pattern  
        cilia_density: Ciliary corona density
        life_stage: Developmental stage
        color_palette: Color scheme
        rendering_style: Visualization approach
    
    Returns:
        Complete fractal specification ready for Claude synthesis,
        including biological origin tracking
    """
    # Step 1: Map anthrobot → fractal (Layer 2)
    mapping = _map_anthrobot_to_fractal_impl(
        morphotype=morphotype,
        symmetry=symmetry,
        movement_type=movement_type,
        cilia_density=cilia_density,
        life_stage=life_stage
    )
    
    # Step 2: Generate fractal parameters (Layer 3)
    fractal_params = _generate_fractal_parameters_impl(
        base_type=mapping['base_fractal_type'],
        recursion_irregularity=mapping['falconer_parameters']['recursion_irregularity'],
        angle_variance=mapping['falconer_parameters']['angle_variance'],
        iteration_depth_variation=mapping['falconer_parameters']['iteration_depth_variation'],
        curve_introduction=mapping['falconer_parameters']['curve_introduction'],
        fractal_dimension=mapping['falconer_parameters']['fractal_dimension'],
        color_palette=color_palette,
        rendering_style=rendering_style
    )
    
    # Add biological provenance
    fractal_params['biological_origin'] = mapping['biological_origin']
    fractal_params['mapping_rationale'] = mapping['mapping_rationale']
    
    # Enhance synthesis guidance with biological context
    original_guidance = fractal_params['synthesis_guidance']
    bio_context = f"""
    BIOLOGICAL ORIGIN: Anthrobot morphology transformation
      Source: {morphotype} anthrobot with {symmetry} symmetry
      Movement: {movement_type} pattern
      Surface: {cilia_density} ciliary corona
      Maturity: {life_stage} stage
    
    TRANSFORMATION: Biological structure → Mathematical fractal
      {mapping['mapping_rationale']['morphotype']}
      {mapping['mapping_rationale']['symmetry']}
      {mapping['mapping_rationale']['movement']}
    """
    
    fractal_params['synthesis_guidance'] = bio_context + "\n" + original_guidance
    
    return fractal_params


@mcp.tool()
def suggest_composition_domains() -> str:
    """
    Suggest other Lushy domains that compose well with fractal morphology.
    
    Returns recommendations for categorical composition.
    """
    compositions = OLOG.get('composition_targets', {})
    
    result = "# Composition Opportunities for Fractal Morphology\n\n"
    
    for domain_name, data in compositions.items():
        result += f"## {domain_name.replace('_', ' ').title()}\n"
        
        result += "**Shared Structure:**\n"
        for struct in data['shared_structure']:
            result += f"- {struct}\n"
        
        if 'functor_mapping' in data:
            fmap = data['functor_mapping']
            result += f"\n**Functor Mapping:**\n"
            result += f"- Fractal complexity → {fmap['complexity_target']}\n"
            result += f"- Recursion pattern → {fmap['pattern_target']}\n"
            result += f"- Surface texture → {fmap['texture_target']}\n"
        
        result += "\n"
    
    return result


@mcp.tool()
def get_research_attribution() -> str:
    """
    Get complete research citations and educational resources.
    
    Returns attribution to Hafız, Falconer, and related research.
    """
    citations = OLOG.get('citations', {})
    
    result = "# Fractal Morph Research Attribution\n\n"
    
    result += "## Primary Mathematical Foundation\n\n"
    result += f"{citations.get('falconer', '')}\n\n"
    
    result += "## Aesthetic Framework\n\n"
    result += f"{citations.get('hafiz_ga2024', '')}\n\n"
    result += f"{citations.get('hafiz_phd', '')}\n\n"
    
    result += "## Related Research\n\n"
    result += f"{citations.get('mennan_nonstandard', '')}\n\n"
    
    result += "## Integration Research\n\n"
    result += f"{citations.get('levin_morphospace', '')}\n"
    
    return result


# ==============================================================================
# PHASE 2.6 - Rhythmic Preset Infrastructure
# ==============================================================================

# 5D normalized parameter morphospace
# Parameters: [recursion_irregularity, angle_variance, iteration_depth_variation,
#              curve_introduction, dimension_intensity]
# dimension_intensity = (fractal_dimension - 1.0) / 2.0  → [0.0, 1.0]

FRACTAL_PARAMETER_NAMES = [
    "recursion_irregularity",
    "angle_variance",
    "iteration_depth_variation",
    "curve_introduction",
    "dimension_intensity"
]

# Canonical states: six morphospace anchors spanning complexity spectrum
FRACTAL_CANONICAL_STATES = {
    "crystalline_order": {
        # Koch snowflake character: rigid, uniform, geometric precision
        "recursion_irregularity": 0.05,
        "angle_variance": 0.05,
        "iteration_depth_variation": 0.10,
        "curve_introduction": 0.05,
        "dimension_intensity": 0.13   # dim ≈ 1.26
    },
    "fractal_cascade": {
        # Sierpinski character: hierarchical voids, recursive removal, fractal dust
        "recursion_irregularity": 0.40,
        "angle_variance": 0.30,
        "iteration_depth_variation": 0.85,
        "curve_introduction": 0.10,
        "dimension_intensity": 0.45   # dim ≈ 1.90
    },
    "spatial_labyrinth": {
        # Hilbert/Peano character: space-filling, maze-like, continuous coverage
        "recursion_irregularity": 0.20,
        "angle_variance": 0.15,
        "iteration_depth_variation": 0.50,
        "curve_introduction": 0.15,
        "dimension_intensity": 0.50   # dim = 2.0
    },
    "organic_branching": {
        # Dragon curve / natural growth: irregular, biomorphic, angle-varied
        "recursion_irregularity": 0.65,
        "angle_variance": 0.75,
        "iteration_depth_variation": 0.60,
        "curve_introduction": 0.70,
        "dimension_intensity": 0.40   # dim ≈ 1.80
    },
    "dimensional_threshold": {
        # Near dimension 2: balanced, complex, on edge of space-filling
        "recursion_irregularity": 0.55,
        "angle_variance": 0.45,
        "iteration_depth_variation": 0.70,
        "curve_introduction": 0.50,
        "dimension_intensity": 0.55   # dim ≈ 2.10
    },
    "sublime_complexity": {
        # Maximum Hafız vastness: all parameters pushed, overwhelming detail
        "recursion_irregularity": 0.90,
        "angle_variance": 0.85,
        "iteration_depth_variation": 0.90,
        "curve_introduction": 0.85,
        "dimension_intensity": 0.75   # dim ≈ 2.50
    }
}

# Five rhythmic presets with strategically chosen periods
# Period strategy:
#   13 — fills gap 12–15 (unique to fractal; creates new LCM pathways)
#   17 — fills gap 16–18 (strengthens known 4-domain novel gap-filler)
#   22 — shared with catastrophe+heraldic (enables 3-domain cross-sync)
#   26 — fills gap 25–30 (unique fractal gap-filler; complements Period 27)
#   32 — harmonic of 16 (2×16, creates resonance with microscopy + heraldic)
FRACTAL_RHYTHMIC_PRESETS = {
    "organic_emergence": {
        "state_a": "crystalline_order",
        "state_b": "organic_branching",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 13,
        "description": "Geometric precision dissolving into biological branching",
        "period": 13,
        "period_rationale": "Gap-filler 12–15; unique fractal signature"
    },
    "complexity_cascade": {
        "state_a": "crystalline_order",
        "state_b": "sublime_complexity",
        "pattern": "sinusoidal",
        "num_cycles": 4,
        "steps_per_cycle": 17,
        "description": "Ordered geometry building toward sublime data density",
        "period": 17,
        "period_rationale": "Strengthens known 4-domain novel attractor (gap 16–18)"
    },
    "space_filling_pulse": {
        "state_a": "fractal_cascade",
        "state_b": "spatial_labyrinth",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 22,
        "description": "Void-filled fragmentation pulsing toward continuous coverage",
        "period": 22,
        "period_rationale": "Cross-domain sync: shared with catastrophe+heraldic"
    },
    "dimensional_drift": {
        "state_a": "organic_branching",
        "state_b": "dimensional_threshold",
        "pattern": "triangular",
        "num_cycles": 2,
        "steps_per_cycle": 26,
        "description": "Biomorphic form drifting through dimensional boundary",
        "period": 26,
        "period_rationale": "Gap-filler 25–30; complements Period 27 (heraldic)"
    },
    "sublime_threshold": {
        "state_a": "spatial_labyrinth",
        "state_b": "sublime_complexity",
        "pattern": "square",
        "num_cycles": 4,
        "steps_per_cycle": 32,
        "description": "Abrupt switching between ordered coverage and infinite complexity",
        "period": 32,
        "period_rationale": "2×16 harmonic; resonates with microscopy+heraldic Period 16"
    }
}

# Visual vocabulary types for nearest-neighbor attractor prompt generation
# Each type has morphospace coordinates and image-generation keywords
FRACTAL_VISUAL_TYPES = {
    "crystalline": {
        "coords": {
            "recursion_irregularity": 0.05,
            "angle_variance": 0.05,
            "iteration_depth_variation": 0.10,
            "curve_introduction": 0.05,
            "dimension_intensity": 0.13
        },
        "keywords": [
            "crystalline fractal precision",
            "hexagonal self-similarity",
            "sharp mathematical edges",
            "uniform recursive depth",
            "rigid geometric branching",
            "snow crystal perfection",
            "deterministic iteration"
        ]
    },
    "fragmented": {
        "coords": {
            "recursion_irregularity": 0.40,
            "angle_variance": 0.30,
            "iteration_depth_variation": 0.85,
            "curve_introduction": 0.10,
            "dimension_intensity": 0.45
        },
        "keywords": [
            "hierarchical void structure",
            "recursive self-similar holes",
            "cantor dust texture",
            "depth-varying articulation",
            "fractal sponge geometry",
            "perforated mathematical mesh",
            "nested removal pattern"
        ]
    },
    "labyrinthine": {
        "coords": {
            "recursion_irregularity": 0.20,
            "angle_variance": 0.15,
            "iteration_depth_variation": 0.50,
            "curve_introduction": 0.15,
            "dimension_intensity": 0.50
        },
        "keywords": [
            "space-filling labyrinth",
            "continuous Hilbert path",
            "maze-like planar coverage",
            "dense meander structure",
            "dimension-2 saturation",
            "systematic space traversal",
            "orderly infinite path"
        ]
    },
    "biomorphic": {
        "coords": {
            "recursion_irregularity": 0.65,
            "angle_variance": 0.75,
            "iteration_depth_variation": 0.60,
            "curve_introduction": 0.70,
            "dimension_intensity": 0.40
        },
        "keywords": [
            "organic fractal branching",
            "Falconer random variation",
            "natural coastline irregularity",
            "biological growth pattern",
            "flowing curved segments",
            "tree-like angle variation",
            "naturalistic self-similarity"
        ]
    },
    "liminal": {
        "coords": {
            "recursion_irregularity": 0.55,
            "angle_variance": 0.45,
            "iteration_depth_variation": 0.70,
            "curve_introduction": 0.50,
            "dimension_intensity": 0.55
        },
        "keywords": [
            "dimensional threshold form",
            "semi-organic complexity",
            "balanced geometry and nature",
            "richly textured boundaries",
            "moderate fractal dimension",
            "intricate but legible structure",
            "complexity at cusp of sublime"
        ]
    },
    "sublime": {
        "coords": {
            "recursion_irregularity": 0.90,
            "angle_variance": 0.85,
            "iteration_depth_variation": 0.90,
            "curve_introduction": 0.85,
            "dimension_intensity": 0.75
        },
        "keywords": [
            "overwhelming fractal data density",
            "infinite detail cascade",
            "Hafız sublime vastness",
            "boundary-dissolving complexity",
            "ultra-fine recursive articulation",
            "perception-exceeding iteration depth",
            "astonishing natural resemblance"
        ]
    }
}


def _generate_oscillation_fractal(num_steps: int, num_cycles: float, pattern: str) -> list:
    """Generate oscillation values in [0, 1] for fractal preset trajectories."""
    import math
    result = []
    for i in range(num_steps):
        t = (2 * math.pi * num_cycles * i) / num_steps

        if pattern == "sinusoidal":
            val = 0.5 * (1 + math.sin(t))
        elif pattern == "triangular":
            t_norm = ((num_cycles * i / num_steps) % 1.0)
            val = 2 * t_norm if t_norm < 0.5 else 2 * (1 - t_norm)
        elif pattern == "square":
            t_norm = ((num_cycles * i / num_steps) % 1.0)
            val = 0.0 if t_norm < 0.5 else 1.0
        else:
            val = 0.5 * (1 + math.sin(t))

        result.append(val)
    return result


def _generate_fractal_preset_trajectory(preset_name: str) -> list:
    """
    Generate complete trajectory for a Phase 2.6 preset.
    Returns list of state dicts, one per step.
    """
    preset = FRACTAL_RHYTHMIC_PRESETS[preset_name]
    state_a = FRACTAL_CANONICAL_STATES[preset["state_a"]]
    state_b = FRACTAL_CANONICAL_STATES[preset["state_b"]]

    num_cycles = preset["num_cycles"]
    steps_per_cycle = preset["steps_per_cycle"]
    total_steps = num_cycles * steps_per_cycle

    alphas = _generate_oscillation_fractal(total_steps, num_cycles, preset["pattern"])

    trajectory = []
    for alpha in alphas:
        state = {}
        for param in FRACTAL_PARAMETER_NAMES:
            state[param] = (1.0 - alpha) * state_a[param] + alpha * state_b[param]
        trajectory.append(state)

    return trajectory


def _euclidean_distance_fractal(state: dict, coords: dict) -> float:
    """Compute Euclidean distance between state and visual type coords."""
    import math
    total = 0.0
    for param in FRACTAL_PARAMETER_NAMES:
        diff = state.get(param, 0.5) - coords[param]
        total += diff * diff
    return math.sqrt(total)


def _extract_fractal_visual_vocabulary(state: dict, strength: float = 1.0) -> dict:
    """
    Extract visual vocabulary for a fractal state via nearest-neighbor matching.

    Args:
        state: Dict with fractal parameter values
        strength: Blend weight [0.0, 1.0]

    Returns:
        Nearest visual type with keywords weighted by strength and distance
    """
    min_dist = float('inf')
    nearest_type = None

    for type_name, type_data in FRACTAL_VISUAL_TYPES.items():
        dist = _euclidean_distance_fractal(state, type_data["coords"])
        if dist < min_dist:
            min_dist = dist
            nearest_type = type_name

    type_data = FRACTAL_VISUAL_TYPES[nearest_type]

    # Scale keyword count by strength
    num_keywords = max(2, round(strength * len(type_data["keywords"])))
    selected_keywords = type_data["keywords"][:num_keywords]

    return {
        "nearest_type": nearest_type,
        "distance": round(min_dist, 4),
        "strength": strength,
        "keywords": selected_keywords,
        "all_types_distances": {
            name: round(_euclidean_distance_fractal(state, data["coords"]), 4)
            for name, data in FRACTAL_VISUAL_TYPES.items()
        }
    }


# ==============================================================================
# PHASE 2.6 TOOLS
# ==============================================================================

@mcp.tool()
def get_canonical_states() -> dict:
    """
    List all canonical fractal states with their 5D morphospace coordinates.

    LAYER 1 TAXONOMY - 0 tokens

    Returns the six anchoring states spanning the fractal complexity spectrum,
    from crystalline mathematical precision to Hafız sublime vastness.

    Morphospace dimensions:
      recursion_irregularity  — uniform recursion ↔ chaotic natural variation
      angle_variance          — rigid angles ↔ wildly organic branching
      iteration_depth_variation — uniform depth ↔ dramatic detail contrast
      curve_introduction      — straight segments ↔ flowing biomorphic curves
      dimension_intensity     — line-like (0.0) ↔ near-volume-filling (1.0)
    """
    result = {
        "parameter_names": FRACTAL_PARAMETER_NAMES,
        "parameter_semantics": {
            "recursion_irregularity": "0.0=uniform Koch-like, 1.0=maximally irregular natural",
            "angle_variance": "0.0=fixed geometric angles, 1.0=wildly varying branching",
            "iteration_depth_variation": "0.0=uniform depth, 1.0=extreme spatial depth contrast",
            "curve_introduction": "0.0=all straight segments, 1.0=all flowing curves",
            "dimension_intensity": "0.0=dim≈1.0 (line), 1.0=dim≈3.0 (volume-filling)"
        },
        "canonical_states": FRACTAL_CANONICAL_STATES,
        "state_descriptions": {
            "crystalline_order": "Koch snowflake precision: uniform, rigid, hexagonally symmetric",
            "fractal_cascade": "Sierpinski character: hierarchical voids, recursive removal",
            "spatial_labyrinth": "Hilbert/Peano space-filling: dense, maze-like, continuous",
            "organic_branching": "Dragon curve / Falconer random: biomorphic, angle-varied, natural",
            "dimensional_threshold": "Near dim-2: balanced complexity on edge of space-filling",
            "sublime_complexity": "Maximum Hafız vastness: all parameters pushed, overwhelming detail"
        }
    }
    return result


@mcp.tool()
def get_rhythmic_presets() -> dict:
    """
    List all Phase 2.6 rhythmic presets with periods and transition descriptions.

    LAYER 1 TAXONOMY - 0 tokens

    Returns five canonical oscillation presets with strategically chosen periods
    designed for cross-domain resonance in multi-domain composition:

      organic_emergence  — period 13 (gap-filler 12–15, fractal signature)
      complexity_cascade — period 17 (strengthens known 4-domain gap-filler)
      space_filling_pulse — period 22 (cross-domain sync: catastrophe+heraldic)
      dimensional_drift  — period 26 (gap-filler 25–30, complements heraldic P27)
      sublime_threshold  — period 32 (2×16 harmonic, resonates microscopy+heraldic)
    """
    result = {
        "presets": {},
        "period_landscape": {
            "fractal_periods": [13, 17, 22, 26, 32],
            "existing_domain_periods": {
                "microscopy": [10, 16, 20, 24, 30],
                "nuclear": [15, 18],
                "catastrophe": [15, 18, 20, 22, 25],
                "diatom": [12, 15, 18, 20, 30],
                "heraldic": [12, 16, 22, 25, 30]
            },
            "gaps_filled_by_fractal": [
                "Period 13: gap between diatom(12) and catastrophe(15)",
                "Period 17: gap between microscopy/heraldic(16) and nuclear(18)",
                "Period 26: gap between heraldic(25) and microscopy/diatom(30)",
                "Period 32: harmonic 2×16 extending beyond existing landscape"
            ],
            "cross_domain_resonances": [
                "Period 22: fractal+catastrophe+heraldic three-domain sync",
                "Period 17: fractal reinforces existing novel 4-domain gap-filler",
                "Period 26: fractal+heraldic(27) adjacent gap competition"
            ]
        }
    }

    for name, preset in FRACTAL_RHYTHMIC_PRESETS.items():
        result["presets"][name] = {
            "period": preset["period"],
            "pattern": preset["pattern"],
            "state_a": preset["state_a"],
            "state_b": preset["state_b"],
            "num_cycles": preset["num_cycles"],
            "steps_per_cycle": preset["steps_per_cycle"],
            "total_steps": preset["num_cycles"] * preset["steps_per_cycle"],
            "description": preset["description"],
            "period_rationale": preset["period_rationale"]
        }

    return result


@mcp.tool()
def apply_rhythmic_preset(
    preset_name: Literal[
        "organic_emergence",
        "complexity_cascade",
        "space_filling_pulse",
        "dimensional_drift",
        "sublime_threshold"
    ],
    num_keyframes: int = 8
) -> dict:
    """
    Apply a Phase 2.6 rhythmic preset and return sampled keyframe states.

    LAYER 2 DETERMINISTIC - 0 tokens

    Generates the complete oscillation trajectory for the requested preset,
    then samples evenly-spaced keyframes for use in image sequence generation.

    Args:
        preset_name: One of the five canonical presets
        num_keyframes: Number of keyframe states to return (2–32)

    Returns:
        Preset metadata, full period info, and sampled keyframe states
        in 5D parameter space ready for generate_fractal_parameters()
    """
    num_keyframes = max(2, min(32, num_keyframes))

    preset = FRACTAL_RHYTHMIC_PRESETS[preset_name]
    trajectory = _generate_fractal_preset_trajectory(preset_name)
    total_steps = len(trajectory)

    # Sample evenly-spaced keyframes
    indices = [round(i * (total_steps - 1) / (num_keyframes - 1))
               for i in range(num_keyframes)]
    keyframes = []
    for idx, step_idx in enumerate(indices):
        state = trajectory[step_idx]
        # Convert dimension_intensity back to fractal_dimension for usability
        fractal_dim = round(1.0 + state["dimension_intensity"] * 2.0, 3)
        keyframe = {
            "keyframe_index": idx,
            "trajectory_step": step_idx,
            "phase_fraction": round(step_idx / (total_steps - 1), 3),
            "parameters": {k: round(v, 4) for k, v in state.items()},
            "fractal_dimension": fractal_dim,
            "complexity_level": (
                "minimal" if state["recursion_irregularity"] < 0.25
                else "moderate" if state["recursion_irregularity"] < 0.50
                else "high" if state["recursion_irregularity"] < 0.75
                else "extreme"
            )
        }
        keyframes.append(keyframe)

    return {
        "preset_name": preset_name,
        "period": preset["period"],
        "pattern": preset["pattern"],
        "state_a": preset["state_a"],
        "state_b": preset["state_b"],
        "total_trajectory_steps": total_steps,
        "description": preset["description"],
        "period_rationale": preset["period_rationale"],
        "num_keyframes": num_keyframes,
        "keyframes": keyframes,
        "usage_note": (
            "Pass keyframe['parameters'] to generate_fractal_parameters() "
            "with dimension_intensity converted: "
            "fractal_dimension = 1.0 + dimension_intensity * 2.0"
        )
    }


# ==============================================================================
# PHASE 2.7 - ATTRACTOR VISUALIZATION PROMPT GENERATION
# ==============================================================================

@mcp.tool()
def generate_attractor_visualization_prompt(
    state: Optional[Dict[str, float]] = None,
    preset_name: Optional[Literal[
        "organic_emergence",
        "complexity_cascade",
        "space_filling_pulse",
        "dimensional_drift",
        "sublime_threshold"
    ]] = None,
    preset_keyframe: int = 0,
    mode: Literal["composite", "split_view", "sequence"] = "composite",
    color_palette: Literal["monochrome", "thermal", "biological", "cosmic"] = "monochrome",
    rendering_style: Literal["line_art", "filled_regions", "gradient_shading", "particle_trace"] = "line_art",
    strength: float = 1.0
) -> dict:
    """
    Generate image-generation prompt from fractal attractor state.

    LAYER 3 SYNTHESIS - uses visual vocabulary nearest-neighbor extraction

    Translates a 5D fractal morphospace position into concrete visual
    descriptors suitable for ComfyUI, Stable Diffusion, or DALL-E.

    Can accept either:
      - A direct state dict (e.g. from apply_rhythmic_preset keyframe)
      - A preset name + keyframe index to auto-sample

    Args:
        state: Dict with fractal parameter values (overrides preset sampling)
        preset_name: Preset to sample from (if state not provided)
        preset_keyframe: Which keyframe to use when sampling preset (0-indexed)
        mode: "composite" = single blended prompt,
              "split_view" = separate prompt per aspect,
              "sequence" = three keyframe progression
        color_palette: Color scheme for prompt
        rendering_style: Rendering approach for prompt
        strength: Vocabulary blend weight [0.0–1.0]

    Returns:
        Generated prompt(s) with vocabulary analysis and composition guidance
    """
    # Resolve state
    if state is None:
        if preset_name is None:
            preset_name = "complexity_cascade"
        trajectory_data = apply_rhythmic_preset(preset_name, num_keyframes=max(8, preset_keyframe + 1))
        kf_idx = min(preset_keyframe, len(trajectory_data["keyframes"]) - 1)
        state = trajectory_data["keyframes"][kf_idx]["parameters"]
        source_info = f"preset '{preset_name}' keyframe {kf_idx}"
    else:
        source_info = "provided state"

    # Extract visual vocabulary
    vocab = _extract_fractal_visual_vocabulary(state, strength=strength)
    nearest_type = vocab["nearest_type"]
    keywords = vocab["keywords"]

    # Get color/rendering descriptors
    palette_def = OLOG['color_palettes'][color_palette]
    render_def = OLOG['rendering_styles'][rendering_style]

    # Compute complexity level for context
    avg_complexity = (
        state.get("recursion_irregularity", 0.5) * 0.30 +
        state.get("angle_variance", 0.5) * 0.20 +
        state.get("iteration_depth_variation", 0.5) * 0.30 +
        state.get("curve_introduction", 0.5) * 0.20
    )
    complexity_level = (
        "minimal" if avg_complexity < 0.25
        else "moderate" if avg_complexity < 0.50
        else "high" if avg_complexity < 0.75
        else "extreme"
    )
    fractal_dim = round(1.0 + state.get("dimension_intensity", 0.5) * 2.0, 2)

    # Natural analogs from complexity and type
    natural_analog_map = {
        "crystalline": "snowflake crystal, geometric frost pattern",
        "fragmented": "recursive sponge, porous coral structure",
        "labyrinthine": "neural pathway network, vascular tree, root system",
        "biomorphic": "coastline, lightning path, tree branch network",
        "liminal": "mountain range silhouette, river delta",
        "sublime": "stormy ocean surface, infinite canyon detail"
    }
    natural_analog = natural_analog_map.get(nearest_type, "natural fractal form")

    if mode == "composite":
        keyword_str = ", ".join(keywords)
        prompt = (
            f"{keyword_str}, {palette_def['description'].lower()}, "
            f"{render_def['description'].lower()}, "
            f"fractal dimension {fractal_dim}, {complexity_level} complexity, "
            f"resembling {natural_analog}, "
            f"Falconer random fractal, Hafız aesthetics of vastness"
        )
        result = {
            "mode": "composite",
            "source": source_info,
            "prompt": prompt,
            "vocabulary_analysis": {
                "nearest_type": nearest_type,
                "distance": vocab["distance"],
                "keywords_used": keywords,
                "complexity_level": complexity_level,
                "fractal_dimension": fractal_dim
            }
        }

    elif mode == "split_view":
        # Separate prompt components for domain-specific use
        structure_prompt = ", ".join(keywords[:3]) + f", fractal dimension {fractal_dim}"
        texture_prompt = ", ".join(keywords[3:]) + f", {complexity_level} complexity surface"
        color_prompt = palette_def["description"].lower() + f", {render_def['description'].lower()}"
        result = {
            "mode": "split_view",
            "source": source_info,
            "prompts": {
                "structure": structure_prompt,
                "texture": texture_prompt,
                "color_rendering": color_prompt,
                "natural_analog": f"resembling {natural_analog}"
            },
            "combined_prompt": f"{structure_prompt}, {texture_prompt}, {color_prompt}",
            "vocabulary_analysis": {
                "nearest_type": nearest_type,
                "distance": vocab["distance"],
                "all_distances": vocab["all_types_distances"]
            }
        }

    elif mode == "sequence":
        # Generate three keyframe prompts for animation/sequence
        if preset_name is None:
            # Infer nearest preset from state
            preset_name = "complexity_cascade"

        traj = apply_rhythmic_preset(preset_name, num_keyframes=3)
        sequence_prompts = []

        for kf in traj["keyframes"]:
            kf_state = kf["parameters"]
            kf_vocab = _extract_fractal_visual_vocabulary(kf_state, strength=strength)
            kf_keywords = ", ".join(kf_vocab["keywords"][:4])
            kf_dim = kf["fractal_dimension"]
            kf_prompt = (
                f"{kf_keywords}, {palette_def['description'].lower()}, "
                f"fractal dimension {kf_dim}, Falconer random fractal"
            )
            sequence_prompts.append({
                "keyframe": kf["keyframe_index"],
                "phase": kf["phase_fraction"],
                "nearest_type": kf_vocab["nearest_type"],
                "prompt": kf_prompt
            })

        result = {
            "mode": "sequence",
            "preset": preset_name,
            "period": FRACTAL_RHYTHMIC_PRESETS[preset_name]["period"],
            "sequence_prompts": sequence_prompts,
            "transition_description": FRACTAL_RHYTHMIC_PRESETS[preset_name]["description"]
        }

    else:
        result = {"error": f"Unknown mode: {mode}"}

    return result


@mcp.tool()
def get_domain_registry_config() -> dict:
    """
    Export fractal domain configuration for Tier 4D multi-domain composition.

    LAYER 1 TAXONOMY - 0 tokens

    Returns the complete domain specification required by the emergent attractor
    discovery system (domain_registry.py). Enables fractal morphology to
    participate in compositional limit cycle discovery alongside microscopy,
    nuclear, catastrophe, diatom, and heraldic domains.

    Period design rationale:
      13 — fills gap 12–15 (unique fractal signature)
      17 — reinforces existing novel 4-domain gap-filler
      22 — shared with catastrophe+heraldic for 3-domain synchronization
      26 — fills gap 25–30 (novel, complements heraldic Period 27)
      32 — 2×16 harmonic, extends beyond existing period landscape
    """
    presets_config = {}
    for name, preset in FRACTAL_RHYTHMIC_PRESETS.items():
        state_a_coords = FRACTAL_CANONICAL_STATES[preset["state_a"]]
        state_b_coords = FRACTAL_CANONICAL_STATES[preset["state_b"]]
        presets_config[name] = {
            "period": preset["period"],
            "pattern": preset["pattern"],
            "state_a_id": preset["state_a"],
            "state_b_id": preset["state_b"],
            "state_a_coords": state_a_coords,
            "state_b_coords": state_b_coords,
            "description": preset["description"],
            "period_rationale": preset["period_rationale"]
        }

    return {
        "domain_id": "fractal",
        "display_name": "Fractal Morphology",
        "description": (
            "Falconer random fractal parameter space encoding Hafız's "
            "aesthetics of vastness — from crystalline mathematical precision "
            "to sublime data-driven complexity"
        ),
        "mcp_server": "fractal-morph-mcp",
        "parameter_names": FRACTAL_PARAMETER_NAMES,
        "parameter_count": len(FRACTAL_PARAMETER_NAMES),
        "canonical_states": FRACTAL_CANONICAL_STATES,
        "canonical_state_count": len(FRACTAL_CANONICAL_STATES),
        "presets": presets_config,
        "periods": [p["period"] for p in FRACTAL_RHYTHMIC_PRESETS.values()],
        "visual_types": {
            name: {
                "coords": data["coords"],
                "keyword_count": len(data["keywords"]),
                "sample_keywords": data["keywords"][:3]
            }
            for name, data in FRACTAL_VISUAL_TYPES.items()
        },
        "period_landscape_analysis": {
            "gaps_filled": [13, 17, 26],
            "shared_periods": [22],
            "harmonics": [32],
            "expected_interactions": {
                "strengthens_existing_novel": "Period 17 (4-domain gap-filler 16–18)",
                "new_three_domain_sync": "Period 22 with catastrophe+heraldic",
                "new_gap_fillers": "Periods 13 and 26 (fractal-unique)",
                "harmonic_resonance": "Period 32 = 2×16 with microscopy+heraldic"
            }
        },
        "composition_compatibility": {
            "high": ["diatom", "catastrophe"],
            "moderate": ["microscopy", "heraldic"],
            "note": (
                "Diatom shares self-similar surface structure; "
                "catastrophe shares geometric singularity character. "
                "Nuclear aesthetics may suppress fractal emergence (known nuclear effect)."
            )
        },
        "registration_snippet": """
# In domain_registry.py initialize_registry():
from fractal_domain import register_fractal_domain
register_fractal_domain()

# Or use get_domain_registry_config() result directly:
# domain_config = fractal_mcp.get_domain_registry_config()
# DOMAIN_REGISTRY['fractal'] = DomainConfig(**domain_config)
        """.strip()
    }


@mcp.tool()
def get_server_info() -> dict:
    """
    Get complete server information including Phase 2.6 and 2.7 capabilities.

    Returns architecture overview, available tools, and integration status.
    """
    return {
        "server": "fractal-morph-mcp",
        "version": "2.0.0",
        "architecture": "Three-layer Lushy + Phase 2.6 rhythmic presets + Phase 2.7 attractor visualization",
        "theoretical_foundation": {
            "primary": "Falconer (2003) - Fractal Geometry: Mathematical Foundations",
            "aesthetic": "Hafız (GA2024) - A New Aesthetics of Vastness",
            "integration": "Lushy Aesthetic Dynamics Framework"
        },
        "layers": {
            "layer_1": {
                "description": "Pure taxonomy retrieval (0 tokens)",
                "tools": [
                    "list_fractal_types",
                    "get_falconer_modifications",
                    "get_complexity_vocabulary",
                    "get_canonical_states",
                    "get_rhythmic_presets",
                    "get_domain_registry_config"
                ]
            },
            "layer_2": {
                "description": "Deterministic computation (0 tokens)",
                "tools": [
                    "map_anthrobot_to_fractal",
                    "compute_fractal_complexity",
                    "apply_rhythmic_preset"
                ]
            },
            "layer_3": {
                "description": "Synthesis preparation (Claude token cost)",
                "tools": [
                    "generate_fractal_parameters",
                    "generate_from_anthrobot",
                    "generate_attractor_visualization_prompt",
                    "get_intentionality_principles",
                    "suggest_composition_domains",
                    "get_research_attribution"
                ]
            }
        },
        "phase_2_6": {
            "status": "complete",
            "canonical_states": list(FRACTAL_CANONICAL_STATES.keys()),
            "presets": {
                name: {
                    "period": p["period"],
                    "pattern": p["pattern"],
                    "description": p["description"]
                }
                for name, p in FRACTAL_RHYTHMIC_PRESETS.items()
            },
            "periods": [13, 17, 22, 26, 32],
            "period_design": "Gap-filling + cross-domain resonance strategy"
        },
        "phase_2_7": {
            "status": "complete",
            "visual_types": list(FRACTAL_VISUAL_TYPES.keys()),
            "prompt_modes": ["composite", "split_view", "sequence"],
            "target_generators": ["ComfyUI", "Stable Diffusion", "DALL-E"],
            "vocabulary_method": "Euclidean nearest-neighbor in 5D morphospace"
        },
        "tier_4d_ready": True,
        "tier_4d_note": (
            "Call get_domain_registry_config() to get complete Tier 4D "
            "registration spec. Fractal periods [13, 17, 22, 26, 32] designed "
            "for maximum emergent attractor novelty across 6-domain compositions."
        )
    }


# Entry point for FastMCP
if __name__ == "__main__":
    mcp.run()
