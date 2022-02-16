#include "ReShade.fxh"

uniform float fUIFarPlane <
	ui_type = "drag";
ui_label = "Far Plane";
ui_tooltip = "RESHADE_DEPTH_LINEARIZATION_FAR_PLANE=<value>\n"
"Changing this value is not necessary in most cases.";
ui_min = 0.0; ui_max = 1000.0;
ui_step = 0.1;
> = 50;

uniform int iUIReversed <
	ui_type = "combo";
ui_label = "Reversed";
ui_items = "RESHADE_DEPTH_INPUT_IS_REVERSED=0\0RESHADE_DEPTH_INPUT_IS_REVERSED=1\0";
> = 1;

float GetDepth(float2 texcoord)
{
	//texcoord.y /= 1.0 / 2.000000001;
	float depth = tex2Dlod(ReShade::DepthBuffer, float4(texcoord, 0, 0)).x;

	if (iUIReversed)
	{
		depth = 1.0 - depth;
	}

	const float N = 1.0;
	return depth /= fUIFarPlane - depth * (fUIFarPlane - N);
}

void PS_DisplayDepth(in float4 position : SV_Position, in float2 texcoord : TEXCOORD, out float3 color : SV_Target)
{
	if (texcoord.x < 0.5 && texcoord.y < 0.5)
	{	
		color = GetDepth(float2(texcoord.x * 2.0, texcoord.y * 2.0)).rrr;
	}
	if (texcoord.x > 0.5 && texcoord.y < 0.5)
	{
		color = tex2D(ReShade::BackBuffer, float2(texcoord.x * 2.0 - 1.0, texcoord.y * 2.0)).rgb;
	}
	if (texcoord.y > 0.5)
	{
		color = 1.0;
	}

}

technique SplitDepth <
	ui_tooltip = "Shader showing depth on half of a screen";
>
{
	pass
	{
		VertexShader = PostProcessVS;
		PixelShader = PS_DisplayDepth;
	}
}
